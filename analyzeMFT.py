#!/usr/bin/python

import analyzemft.mftsession as mftsession

if __name__ == "__main__":
    session = mftsession.MftSession()
    session.mft_options()
    session.open_data()
    session.process_mft_file()
