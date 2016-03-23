# tdo-server

This is a server that helps to manage your tdo lists synced on all your devices.  
You can set up your own or just use the one we will be setting up.


## Development Environment

If you want to work on this project, there are two possibilities:

### Using Vagrant

If you have [Vagrant](https://vagrantup.com) installed, simply run `vagrant up`
in the repository folder on your machine to get started. Vagrant will take care of installing all dependencies.

If your VM is up and running, you can ssh into the machine using `vagrant ssh`.
Start the Django application (living in /home/vagrant/tdoserver) with the command:
```shell
$ python3 manage.py runserver 0.0.0.0:8000
```

It's now accessible via [192.168.33.10:8000](http://192.168.33.10:8000) in your browser.

### The old-fashioned way

1. Make sure you have the latest version of [Python3](https://python.org) and pip installed.
2. Install all dependencies using `pip3 install -r requirements.txt`
3. Run the Django server from your terminal using:  
`$ python3 manage.py runserver`
4. Access the application via [127.0.0.1:8000](http://127.0.0.1:8000).


## TODOs:

- [ ] Create backend
- [ ] make it secure
- [ ] manage Accounts/Logins
- [ ] adding notfication functionality
- [ ] adding Template
