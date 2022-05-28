import os
import time
os.system("clear")

print('Welcome to Nick\'s Apache2 server menu. \nThe purpose of this project is to make DIY web servers \nmore acessable to those who aren\'t fluent in CLI.')
print('Version: Pre-Beta')
print('-----------------------------------------------------------')
menu_options = {
    0: 'Exit',
    1: 'Start Server',
    2: 'Stop Server',
    3: 'Server Status',
    4: 'Run Basic Installs',
    5: 'Run Updates',
    6: 'Apache Tutorial',
    7: 'Test Site With Text Browser',
    8: 'Run Full System AV Scan'
}

def print_menu():
	for key in menu_options.keys():
		print (key, '--', menu_options[key] )

def option1():
	os.system("clear")
	print(' 1 selected \n Starting apache server...')
	os.system("sudo service apache2 start")

def option2():
	os.system("clear")
	print(' 2 selected \n Stopping apache server...')
	os.system("sudo service apache2 stop")

def option3():
	os.system("clear")
	print(' 3 selected \n Reading out server status...')
	print('----------------------------------------------------------')
	os.system("apache2ctl status")

def option4():
	os.system("clear")
	print(' 4 Installing basic programs...')
	os.system("sudo apt install apache2 clamav net-tools traceroute lynx")
	os.system("sudo snap install btop")
	print('DONE')

def option5():
	os.system("clear")
	print(' 5 Running updates...')
	os.system("sudo apt update")
	os.system("sudo apt upgrade")

def option6():
	print('(incomplete)')

def option7():
    os.system("clear")
    os.system("lynx /var/www/html/index.htm")

def option8():
    print("Scanning...")
    os.system("cd /")
    os.system("clamscan *")

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 0:
            print('Goodbye')
            time.sleep(1.5)
            exit()
        elif option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        elif option == 7:
            option7()
        elif option == 8:
            option8()

        else:
            print('Invalid option. Please enter a number between 1 and 6.')
