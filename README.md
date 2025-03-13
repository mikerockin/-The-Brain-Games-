### Hexlet tests and linter status:
[![Actions Status](https://github.com/mikerockin/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/mikerockin/python-project-lvl1/actions)
<a href="https://codeclimate.com/github/mikerockin/python-project-lvl1/maintainability"><img src="https://api.codeclimate.com/v1/badges/400b3120991f564ffe77/maintainability" /></a>
#  "The Brain Games" #

### 1.  Game: "Evenness Check." ##
The user is shown a random number and needs to answer yes if the number is even, or no if it is odd.

Demo: https://asciinema.org/a/mnxohTWHVrZflCYWlmYwexnTR
 
### 2.  Game: "Calculator" ##
The user is shown a random mathematical expression, such as 35 + 16, which they must calculate and write down the correct answer..

Demo: https://asciinema.org/a/MZDy61yK5M6eusHWNmSGwFVqR

### 3.  Game "Least common divisor" ##
The user is shown two random numbers, for example 25 50. The user must calculate and enter the greatest common divisor of these numbers.

Demo: https://asciinema.org/a/096dWTLL6ZTV2H9FJ8CicaF63

### 4.  Game "Arithmetic progression" ##
The user is shown a series of numbers that form an arithmetic progression, one of the numbers in the sequence is replaced by two dots. The player must determine this number.

Demo: https://asciinema.org/a/x07Q9qFbihjuRntjzczyAIgNC

### 5.  Game "Is it a prime number?" ##
The user is shown a number and must determine whether the number is prime and give an answer.

 Demo: https://asciinema.org/a/ECeGKY2ptqHDhq0cU7kVuW7oh

### Installation: ##

- The application container is available on Docker Hub under the name: mikerockin1988/my-brain-games

  https://hub.docker.com/r/mikerockin1988/my-brain-games
  
      $ docker pull mikerockin1988/my-brain-games:1.0
  **After pulling the image, you can run the container in one of 2 modes:
  
I. Interactive:

      $ docker run -it --rm my-brain-games:1.0 sh
  After launch use commands from "**Startup commands**"

II. Launching a specific game:

     $ docker run -it --rm my-brain-games:1.0 <Startup command>

Example:

     $ docker run -it --rm my-brain-games:1.0 brain-even
     $ docker run -it --rm my-brain-games:1.0 brain-calc
     .....
          
- The application container is available on Container Registry ( Yandex Cloud ), access to the Docker image for authorized Yandex Cloud users who are members of the organization**

      $ docker pull cr.yandex/crpv85vhagh6a4tpo9mi/my-brain-games:1.0


## Startup commands: ##
    
    brain-even       - Game: "Evenness Check."

    brain-calc       - Game: "Calculator"

    brain-gcd        - Game "Least common divisor"

    brain-prog       - Game "Arithmetic progression"

    brain-prime      - Game "Is it a prime number?"




