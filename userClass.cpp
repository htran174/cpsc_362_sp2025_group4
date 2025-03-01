/*
======================================================================================
                                    userClass.cpp
                                Created by Hien Tran
                                Last modify: 02/28/2025
                                Bugs: Currently None
    Purpose: Class holds user username, full name ,email, password, address
=======================================================================================
*/
#include <iostream>

using namespace std;

class User 
{
private:
    string username; //user name
    string full_name; //legal name
    string email; //their email
    string password; // password
    string address; //address

public:
    // Constructor
    User(string uname, string lname ,string mail, string pass, string addr)
        : username(uname), email(mail), password(pass), address(addr), full_name(lname) {}

    // Getter methods
    string getUsername() const { return username; }
    string getEmail() const { return email; }
    string getAddress() const { return address; }
    string getFullName() const {return full_name;}

    // Setter methods
    void setUsername(string uname) 
    { 
        username = uname; 
    }

    void setFullName(string lname)
    {
        full_name = lname;
    }

    void setEmail(string mail) 
    { 
        //Have a function connecting to email vefication here
        email = mail; 
    }
    void setPassword(string pass) 
    { 
        //hava a function connecting to hash
        password = pass; 
    }
    void setAddress(string addr) 
    { 
        address = addr; 
    }

    // Method to display user information
    void displayUserInfo() const 
    {
        cout << "Username: " << username << endl;
        cout << "Full Name: " << full_name << endl;
        cout << "Email: " << email << endl;
        cout << "Address: " << address << endl;
    }
};

int main() {
    // Creating a user object
    User user1("htran","Hien Tran" ,"hien@example.com", "securepass123", "123 maple st");

    // Displaying user info
    user1.displayUserInfo();

    return 0;
}
