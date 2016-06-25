# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

# read4(buf) is to read characters from a file to buf. file has endless characters.
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        eof = False
        buffer = [""]*4
        total = 0

        while not eof and total < n:
            count = read4(buffer)
            eof = count < 4
            actualLen = min(count, n-total)
            for i in range(actualLen):
                buf[total] = buffer[i]
                total += 1

        return total
