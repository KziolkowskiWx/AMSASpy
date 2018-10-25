import pandas as pd


def main():
    
    print ('Welcome to AMSASpy. Your at home AMSAS!')
    print ('\n')
    print ('Use as you would use AMSAS but enter q to exit the program!')
    print ('\n')
    
    while True:
        site = input('>> ').upper()
        
        print ('\n')
        if site == 'Q':
            break
            
        try:
            address = 'http://weather.rap.ucar.edu/surface/index.php?metarIds='+site+'&hoursStr=past+12+hours&std_trans=standard&num_metars=number&submit_metars=Retrieve'
        
        except:
            print ('Site does not exist in NCAR database. Try another site.')
            
            
        metar_raw = pd.read_html(address)[0]
        metar = metar_raw[0][1].split(site)
        del metar[0]
        
        
        for i in reversed(metar):
            print (site + i)
        
        print ('\n')
 
if __name__ == '__main__':
    main()
