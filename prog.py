# Author: Lawrence Chillrud <lgc2139@columbia.edu>
# Date: 3/1/20

'''
Fancy progress bar function I just wanted to try out. Code for this function taken from:
https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
'''
def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def test(alphas, x_train, y_train, x_test, y_test, num_classes=10):
    n = x_test.shape[0]
    printProgressBar(0, n, prefix = 'Progress:', suffix = 'Complete', length = 25) # progress bar
    for i in range(n):
        printProgressBar(i, n, prefix = 'Progress:', suffix = 'Complete', length = 25) # progress bar

    printProgressBar(n, n, prefix = 'Progress:', suffix = 'Complete', length = 25) # progress bar

