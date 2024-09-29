from time import time

def typingErrors(prompt, iprompt):
    words = prompt.split()
    iwords = iprompt.split()
    errors = 0
    for i in range(len(iwords)):
        if i in (0, len(iwords)-1):
            if iwords[i] == words[i]:
                continue
            else:
                errors += 1
        else:
            if iwords[i] == words[i]:
                if (iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

def typingSpeed(iprompt, time_elapsed):
    iwords = iprompt.split()
    twords = len(iwords)
    speed = twords / (time_elapsed / 60)
    return speed

def timeElapsed(stime, etime):
    return etime - stime

if __name__ == '__main__':
    prompt = input("Enter the prompt: ")
    input("Press ENTER when you are ready to start typing!")

    stime = time()
    iprompt = input()
    etime = time()

    time_elapsed = round(timeElapsed(stime, etime), 2)
    speed = typingSpeed(iprompt, time_elapsed)
    errors = typingErrors(prompt, iprompt)

    print("Total Time elapsed: ", time_elapsed, "s")
    print("Your Average Typing Speed was: ", speed, "words/minute")
    print("With a total of: ", errors, "errors")
