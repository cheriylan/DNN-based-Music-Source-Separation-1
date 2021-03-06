class CONSTS:
    """Contains constants of the problem"""

    WINDOW_SIZE = 4096
    HOP_SIZE = 1024
    OVERLAP = WINDOW_SIZE - HOP_SIZE
    RATE = 44100
    CONTEXT_SIZE = 5
    FFT_BINS = 2049
    TARGETS = ['vocals', 'drums', 'bass', 'other']
    DB_PATH = './DSD100subset'
    ESTIMATES_PATH = './Estimates'
    AMPLITUDE_MEAN = 0.00049
    AMPLITUDE_STD = 0.00204
    EPOCHS = 20
    BATCH_SIZE = 16
