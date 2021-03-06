#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Nov 18 13:48:01 2014
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 10
        self.samp_rate = samp_rate = 1e6
        self.rx_gain = rx_gain = 10
        self.mclk = mclk = 30e6
        self.items = items = 10000000
        self.center_freq = center_freq = 915e6

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0.set_clock_rate(mclk, uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0.set_center_freq(center_freq, 1)
        self.uhd_usrp_source_0.set_gain(rx_gain, 1)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_sink_0.set_clock_rate(mclk, uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0.set_center_freq(center_freq, 1)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 1)
        self.blocks_head_0_0_0 = blocks.head(gr.sizeof_gr_complex*1, items)
        self.blocks_head_0_0 = blocks.head(gr.sizeof_gr_complex*1, items)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, items)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/kampianakis/Dropbox/MainRepo/Projects/B210_Testbed/Data/data_tx1", True)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/kampianakis/Dropbox/MainRepo/Projects/B210_Testbed/Data/data_rx2", False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/kampianakis/Dropbox/MainRepo/Projects/B210_Testbed/Data/data_rx1", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_head_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_head_0_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_head_0_0_0, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_head_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 1), (self.blocks_head_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.uhd_usrp_sink_0, 1))



    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 0)
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 1)

    def get_mclk(self):
        return self.mclk

    def set_mclk(self, mclk):
        self.mclk = mclk

    def get_items(self):
        return self.items

    def set_items(self, items):
        self.items = items
        self.blocks_head_0_0.set_length(self.items)
        self.blocks_head_0_0_0.set_length(self.items)
        self.blocks_head_0.set_length(self.items)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.uhd_usrp_source_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.center_freq, 1)
        self.uhd_usrp_sink_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.center_freq, 1)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Run(True, 1024)
