def read():
    buf0=['0x01', '0x00', '0x00']
    spi.transfer(buf0,len(buf0))
    print('{0:03d} {1:03d} {2:03d}').format(buf0[0],buf0[1],buf0[2])
