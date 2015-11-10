'''
Created on Nov 10, 2015

@author: rjw366
'''
import numpy as np
import inputValidation as valid
import matplotlib.pyplot as plt
import sys

if __name__ == '__main__':
    try:
        #Parse and validate input
        positions = raw_input("Enter your list of investment numbers? i.e. [1, 10, 100, 1000]")
        positions = valid.positionValidation(positions)
        num_trials = raw_input("Enter the number of trials?")
        num_trials = int(valid.numTrialValidation(num_trials))
        
        #Create values
        position_values = [1000/position for position in positions]
        daily_ret = []
        trial_sum = 0
        #Run the number of trials
        while (num_trials > 0):
            winsPerPosition = [0,0,0,0]
            #Run for each investment position
            for ix,i in enumerate(positions):
                wins = 0
                for j in range(i):
                    chance = np.random.rand()
                    if(chance>.49):
                        wins += 1
                winsPerPosition[ix] = wins
            #Change to numpy arrays to allow for calculation
            winsPerPositionNP = np.array(winsPerPosition)
            position_valuesNP = np.array(position_values)
            cum_ret = []
            cum_ret = (winsPerPositionNP * position_valuesNP * 2)
            daily_ret.append(((cum_ret/1000.0) - 1).tolist())
            num_trials -= 1
        daily_ret =np.array(daily_ret)
        
        #Begin output
        results = open('results.txt','w')
        for ix,i in enumerate(positions):
            #Build then write string
            positionOutput = "Position: " + str(i) + ", Mean = " + str(np.mean(daily_ret[:,ix])) + ", Std Dev = " + str(np.std(daily_ret[:,ix]))
            results.write(positionOutput + '\n')
            
            #Build then write histograms
            plot = plt.figure()
            plt.hist(daily_ret[:,ix], 100, range=[-1,1])
            plot.savefig('histogram_' + str(i).zfill(4) + '_pos.pdf')
            plt.clf()
        results.close()
    
    except ValueError as e:
        print 'There was an error with your input: ' + str(e)
    except KeyboardInterrupt:
        print "Program ended via keyboard"
        sys.exit(1)
    