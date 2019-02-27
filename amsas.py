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


        if len(site) == 3:
            canadian = 'C' + site
            american = 'K' + site

            #check the site
            xc = check(canadian)
            xk = check(american)

            if xc == True:
                address = 'http://weather.rap.ucar.edu/surface/index.php?metarIds='+canadian+'&hoursStr=past+12+hours&std_trans=standard&num_metars=number&submit_metars=Retrieve'
                site = canadian
            elif xk == True:
                address = 'http://weather.rap.ucar.edu/surface/index.php?metarIds='+american+'&hoursStr=past+12+hours&std_trans=standard&num_metars=number&submit_metars=Retrieve'
                site = american
            else:
                address = False


        else:
            canadian = check(site)
            american = check(site)

            if canadian == True:
                address = 'http://weather.rap.ucar.edu/surface/index.php?metarIds='+site+'&hoursStr=past+12+hours&std_trans=standard&num_metars=number&submit_metars=Retrieve'

            elif american == True:
                address = 'http://weather.rap.ucar.edu/surface/index.php?metarIds='+site+'&hoursStr=past+12+hours&std_trans=standard&num_metars=number&submit_metars=Retrieve'

            else:
                address = False




#        address, site = getCanadian_site(site)
        if address == False:
            print ('Site does not exist in NCAR database. Try another site.')

        else:
            metar_raw = pd.read_html(address)[0]
            metar = metar_raw[0][1].split(site)
            del metar[0]
            for i in reversed(metar):
                print (site + i)

        print ('\n')

#---------------------------FUNCTIONS------------------------------------------


def check(site):
    """
    Check to see if the site exists.
    """
    address = 'http://weather.rap.ucar.edu/surface/index.php?metarIds='+site+'&hoursStr=past+12+hours&std_trans=standard&num_metars=number&submit_metars=Retrieve'

    metar_raw = pd.read_html(address)[0]
    if len(metar_raw) == 1:
        checker = False
    else:
        checker = True

    return checker






main()
