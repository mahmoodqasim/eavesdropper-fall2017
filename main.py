from __future__ import division
import numpy as np
import scipy
import matplotlib.pylab as plt

# Let's first make the BPSK signal

Bit_Sequence_Unipolar = np.array([1, 0, 1, 1, 0]) # Bit sequence
Bit_Sequence_Bipolar = 2*Bit_Sequence_Unipolar - 1 # Make it bipolar

bit_duration = 1 # T in the equation
amp = 1 # Amplitude scaling factor
freq_Carrier = 3/bit_duration  # Carrier frequency

spacing = 1000 # Spacing between the time, resolution

time = np.linspace(0, 5, spacing) # Time 0 to 5
samples_per_bit = spacing/Bit_Sequence_Bipolar.size  # Samples per bit

dw = np.repeat(Bit_Sequence_Unipolar, samples_per_bit)  # replicate each sequence as many times as the samples per bit
bw = np.repeat(Bit_Sequence_Bipolar, samples_per_bit)  # replicate each sequence as many times as the samples per bit

General_BPSK = np.sqrt(2*amp/bit_duration) * np.cos(2*np.pi * freq_Carrier * time) # General formula for BPSK
BPSK_with_bits = bw*General_BPSK # Actual BPSK signal

# Now we will add noise

noise_Amp = 0.2
noise = (np.random.randn(len(BPSK_with_bits))+1)*noise_Amp # creating noise of length of BPSK signal using Standard distribution

snr = 10*np.log10(np.mean(np.square(BPSK_with_bits)) / np.mean(np.square(noise))) # SNR Signal to Noise Ratio
print "SNR = %fdB" % snr

BPSK_with_noise = np.add(BPSK_with_bits,noise) # Adding noise to the signal

number_Of_Ones = [i for i in BPSK_with_bits if i >= 0] # Calculating how many 1's were actually sent
BPSK_receiver = [i for i in BPSK_with_noise if i >= 0] # Calculating how many 1's were received

print len(number_Of_Ones) , len(BPSK_receiver) # Printing above

f, ax = plt.subplots(5,1, sharex=True, sharey=True, squeeze=True) # Plotting all of it
ax[0].plot(time, dw)
ax[1].plot(time, bw)
ax[2].plot(time, General_BPSK)
ax[3].plot(time, BPSK_with_bits)
ax[4].plot(time, BPSK_with_noise)
ax[4].axis([0, 5, -1.5, 1.5])
ax[4].set_xlabel('time')
plt.show()
