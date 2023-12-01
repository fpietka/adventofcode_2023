package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "regexp"
    "strconv"
)

func main() {
    file, err := os.Open("input_01")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)

    mapping := map[string]string{
        /*
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        */
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9"}
    
    //expression := "one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9"
    expression := "1|2|3|4|5|6|7|8|9"

    result := 0

    for scanner.Scan() {
        str := scanner.Text()
        re := regexp.MustCompile(expression)

        var chars []string

        for index := 0; index <= len(str); index++ {
            found := re.FindString(str[index:])
            if found != "" {
                chars = append(chars, found)
            }
        }
        number, _ := strconv.Atoi(mapping[chars[0]] + mapping[chars[len(chars)-1]])
        result = result + number
    }

    fmt.Println(result)

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
}
