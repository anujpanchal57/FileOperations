# BW tells that its a binary file and we have to write it into BIN_FILE
with open("binary", 'bw') as bin_file:
    # Prints out the numbers from 0 to 16
    for i in range(17):
        # This line converts the decimal numbers into their respective byte format ,
        # which is then written in the file
        bin_file.write(bytes([i]))

# Alternative for above code
# We get the exactly same result, because instead of looping we are giving it a range of 0-16 directly
with open("binary", 'bw') as bin_file:
    bin_file.write(bytes(range(17)))


# This helps to read the binary from the file and print it on the screen
with open("binary", 'br') as binFile:
    for b in binFile:
        print(b)

# Given as the numbers and on the RHS are their HEX equivalents

a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 02 2D C0 1E

with open("binary2", 'bw') as bin_file:
    # In TO_BYTES method 2 parameters are passed, first one is 'how many bytes we want ? ' and
    # second one is 'BIG or LITLLE Endian how do we want it'
    # BIG ENDIAN stores the most significant byte first and then the least significant ones
    # LITTLE ENDIAN is exactly the opposite of BIG ENDIAN, it stores the least significant bytes first
    # and then the most significant ones
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))

# Now, we'll read all those numbers from the bytes format to integer format
with open("binary2", 'br') as bin_file:
    # FROM_BYTES converts the value from binary to int
    e = int.from_bytes(bin_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big')
    print(i)
