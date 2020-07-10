# -*- coding: utf-8 -*-

import io
import json
import uuid
from time_utils import timestamp_to_date,current_time
import requests
import collections
import re
import logging
import codecs
from date_chunk_handle_class import Date_chunk_handle


class Extract_Schema:

    def __init__(self):
        self.event_flag = 0

        self.conference_rgx = []
        self.adjust_norm_rgx = []
        self.data_shift_rgx = []
        self.buyback_rgx = []
        self.schema_all = []

        self.adjust_norm_rgx_index = {}
        self.data_shift_rgx_index = {}
        self.conference_rgx_index = {}
        self.buyback_rgx_index = {}

        self.conference_schema = {}
        self.adjust_norm_schema = {}
        self.buyback_schema = {}
        self.data_shif_schema = {}

        for rgx in self.adjust_norm_rgx:
            self.adjust_norm_rgx_index[rgx] = [1,2,3]

        for rgx in self.data_shift_rgx:
            self.data_shift_rgx_index[rgx] = [1,2,3]

        for rgx in self.conference_rgx:
            # if rgx == 1:
            self.conference_rgx_index[rgx] = [1,2,3]

        for rgx in self.buyback_rgx:
            # if rgx == 1:
            self.buyback_rgx_index[rgx] = [1,2,3]


    def get_schema_all(self, s, title):
