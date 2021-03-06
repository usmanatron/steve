#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


VOTE_TYPES = (
    
)

DB_TYPES = (
    
)

def appendVote(*types):
    """ Append a new type of voting to the list"""
    global VOTE_TYPES
    for t in types:
        found = False
        for v in VOTE_TYPES:
            if v['key'] == t['key']:
                found = True
                break
        if not found:
            VOTE_TYPES += (t,)
        
def appendBackend(t, c):
    """Append a new database backend"""
    global DB_TYPES
    found = False
    for b in DB_TYPES:
        if b.get('id') == t:
            found = True
            break
    if not found:
        DB_TYPES += ( {
            'id': t,
            'constructor': c
        },)
    
            
def initBackend(config):
    # Set up DB backend
    backend = None
    
    if config.has_option("database", "disabled") and config.get("database", "disabled") == "true":
        return
    dbtype = config.get("database", "dbsys")
    for b in DB_TYPES:
        if b.get('id') == dbtype:
            backend = b['constructor'](config)
            break
    
    if not backend:
        raise Exception("Unknown database backend: %s" % dbtype)
    return backend

# For vote types with N number of seats/spots, this value denotes
# the max number of useable types to display via the API
MAX_NUM = 10