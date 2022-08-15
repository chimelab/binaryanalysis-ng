meta:
  id: lrzip
  title: LRZIP
  license: CC0-1.0
  endian: le
doc-ref:
  - https://github.com/ckolivas/lrzip/blob/master/doc/magic.header.txt
seq:
  - id: header
    type: header
  - id: rchunks
    type: rchunk
    repeat: until
    repeat-until: _.eof_flag == 1
types:
  header:
    seq:
      - id: magic
        contents: "LRZI"
      - id: major_version
        type: u1
      - id: minor_version
        type: u1
      - id: size_or_salt
        type: u8
      - id: unused1
        size: 2
      - id: lzma_properties
        type: u1
      - id: lzma_dictionary
        type: u4
      - id: md5_stored
        type: u1
      - id: encrypted
        type: u1
        valid:
          any-of: [0, 1]
      - id: unused2
        size: 1
  rchunk:
    seq:
      - id: byte_width
        type: u1
      - id: eof_flag
        type: u1
      - id: len_uncompressed
        size: byte_width
      - id: stream_header_0
        type: stream_header(byte_width)
      - id: stream_header_1
        type: stream_header(byte_width)
      - id: ucomp_header
        type: stream_header(byte_width)
  stream_header:
    params:
      - id: len_elem
        type: u1
    seq:
      - id: compressed_data_type
        type: u1
        enum: compressed
      - id: len_compressed
        size: len_elem
      - id: len_uncompressed
        size: len_elem
      - id: next_block_head
        size: len_elem
enums:
  compressed:
    3: no_compression
    4: bzip2
    5: lzo
    6: lzma
    7: gzip
    8: zpaq
