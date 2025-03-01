#include <iostream>

using namespace std;

class User 
{
private:
    string username;
    string email;
    string password;
    string address;

public:
    // Constructor
    User(string uname, string mail, string pass, string addr)
        : username(uname), email(mail), password(pass), address(addr) {}

    // Getter methods
    string getUsername() const { return username; }
    string getEmail() const { return email; }
    string getAddress() const { return address; }

    // Setter methods
    void setUsername(string uname) 
    { 
        username = uname; 
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
        cout << "Email: " << email << endl;
        cout << "Address: " << address << endl;
    }
};

int main() {
    // Creating a user object
    User user1("hientran", "hien@example.com", "securepass123", "123 maple st");

    // Displaying user info
    user1.displayUserInfo();

    return 0;
}
