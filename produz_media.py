import csv

TOTAL_SAMPLES = 8

FILES = [
    #'2.0.1.csv',
    #'2.7.18.csv',
    #'3.0.1.csv',
    #'3.9.21.csv',
    #'3.10.16.csv',
    #'3.11.11.csv',
    #'3.12.3.csv',
    #'3.12.8.csv',
    #'3.12.9.csv',
    #'3.13.1.csv',
    #'3.13.2.csv',
    #'nuitka.csv',
    #'codon_release.csv'
]

def main():

    sample = {} # { path: [(watts, time, memory), ..], ..}

    # Collect data
    for path in FILES:

        sample[path] = []

        with open(path, newline='\n') as file:
            rapl = csv.reader(file, delimiter=',')

            # watts -> time

            i = 0 #row no.
            for I in rapl:
                if i >= 1 and i <= 10: #jump header
                    sample[path].append ( (I[3], I[7], I[9]) ) #[(watts, time, memory), ..]
                i += 1

    # Remove outliers
    for k in sample:

        sample[k].sort(key=lambda e: e[0]) #[(watts,time,memory), ..]
    
        sample[k] = sample[k][1:9] #remove outliers -- min. & max.
    
    # Mean data
    for k in sample:

        mean_w = 0.0 #watts
        mean_t = 0.0 #time
        mean_m = 0.0 #memory

        for w_t in sample[k]:
            mean_w += float (w_t[0])
            mean_t += float (w_t[1])
            mean_m += float (w_t[2])

        mean_w /= TOTAL_SAMPLES    
        mean_t /= TOTAL_SAMPLES    
        mean_m /= TOTAL_SAMPLES
        
        sample[k] = (mean_w, mean_t, mean_m)

    # Otput data
    for k,v in sample.items():
        print(f"{k} | {v[0]:.0f} watts | {v[1]:.0f} ms | {v[2]:.0f} KBytes", end="\n")


if __name__ == "__main__":
    main()
