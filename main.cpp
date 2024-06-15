#include <algorithm>
#include <chrono>
#include <cassert>
#include <random>
#include <fstream> // Include for file operations
#include <iostream>
#include <vector>
#include <string>

#include "brute_force.h"
#include "SundayMatching.h"
#include "kmp.h"
#include "FSM.h"
#include "rabin-karp.h"
#include "Zalgorithm.h"

using std::chrono::nanoseconds;

const int times = 10;

// Function to generate random text of given size
std::string generateRandomText(size_t length) {
    static std::default_random_engine engine((std::random_device())());
    static std::uniform_int_distribution<int> char_dist(32, 126); // Printable ASCII characters

    std::string random_text;
    random_text.reserve(length);

    for (size_t i = 0; i < length; ++i) {
        random_text.push_back(static_cast<char>(char_dist(engine)));
    }

    return random_text;
}

nanoseconds timeit(std::string& pat, std::string& txt, std::vector<int>(*what)(std::string&, std::string&)) {
    auto begin = std::chrono::steady_clock::now(); // Start timing
    what(pat, txt); // Run the pattern matching algorithm
    auto end = std::chrono::steady_clock::now(); // Stop timing

    return std::chrono::duration_cast<nanoseconds>(end - begin); // Convert duration to microseconds
}

int main() {
    std::vector<size_t> text_lengths = { 1000, 20000, 40000, 60000, 80000}; // Different text sizes to test
    std::string pattern = "the lemon world";

    std::ofstream outfile("data_with_phrases.txt"); // Open a file for writing the data

    // Check if the file is open
    if (!outfile.is_open()) {
        std::cerr << "Error opening file!" << std::endl;
        return 1; // Exit with an error code
    }

    outfile << "Text Size,Algorithm,Average Time (nanoseconds)\n"; // CSV header

    for (auto text_length : text_lengths) { // Loop over each text size
        std::string text = generateRandomText(text_length); // Generate random text of given size

        nanoseconds bruteforce_time(0);
        nanoseconds sunday_time(0);
        nanoseconds kmp_time(0);
        nanoseconds finite_automata_time(0);
        nanoseconds rabin_karp_time(0);
        nanoseconds gusfield_z_time(0);

        // Repeat the measurements multiple times
        for (int t = 0; t < times; ++t) {
            bruteforce_time += timeit(pattern, text, &bruteforce);
            sunday_time += timeit(pattern, text, &sundaySearch);
            kmp_time += timeit(pattern, text, &kmp);
            finite_automata_time += timeit(pattern, text, &patternMatching);
            rabin_karp_time += timeit(pattern, text, &rabin_karp);
            gusfield_z_time += timeit(pattern, text, &Z_matching);
        }

        // Write the average times for each algorithm and text size to the file
        outfile
            << text_length << ",Brute Force," << bruteforce_time.count() / times << "\n"
            << text_length << ",Sunday," << sunday_time.count() / times << "\n"
            << text_length << ",KMP," << kmp_time.count() / times << "\n"
            << text_length << ",FSM," << finite_automata_time.count() / times << "\n"
            << text_length << ",Rabin-Karp," << rabin_karp_time.count() / times << "\n"
            << text_length << ",Gusfield Z," << gusfield_z_time.count() / times << "\n";
    }

    outfile.close(); // Close the file

    std::cout << "Data written to data.txt" << std::endl;

    return 0; // Exit successfully
}
