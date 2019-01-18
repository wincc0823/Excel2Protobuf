# Excel2Protobuf
##
# @file:   excel_to_protobuf.py
# @author:  Triniti Interactive Limited
# Copyright (c) Triniti Interactive Limited All rights reserved.
#
# This code is licensed under the MIT License (MIT).
# THIS CODE IS PROVIDED *AS IS* WITHOUT WARRANTY OF
# ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY
# IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR
# PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.
# brief:  export excel to protobuf
##
# 1. Make sure the form name is in English and begins with an uppercase letter
# 2. Make sure that the first column of all tables is a unique index
#
# parameters
# -i --input_path input folder which contains excel files to convert.
#       This script converts all excel file from that folder
# -d --data_out folder where serialized binary protobuf file exported
# -n --name_space specific the namespace of the exported code
# -c --csharp_out folder where auto generated C# script file(from protoc.exe) exported
# -s --server folder where auto generated server script file(from protoc.exe) exported
# -l --Server-side programm language eg.(cpp|csharp|java|go|js|objc|php|python|ruby )
# -p --java out package name 
##