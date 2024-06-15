#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

std::string readFile(const std::string& filePath) {
    std::ifstream file(filePath);  // Create an input file stream
    if (!file.is_open()) {         // Check if the file was successfully opened
        return "File not found. Please check the file path.";
    }
    
    std::stringstream buffer;      // Create a string stream to hold the file content
    buffer << file.rdbuf();        // Read the file content into the string stream
    file.close();                  // Close the file
    
    return buffer.str();           // Convert the string stream to a string and return it
}

int main() {
    std::string filePath = "100words.txt";  // Replace with your file path
    std::string content = readFile(filePath);
    std::cout << content << std::endl;
    
    return 0;
}
