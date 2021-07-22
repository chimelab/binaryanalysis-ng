meta:
  id: erofs
  title: Enhanced Read-Only File System
  license: Apache-2.0
  endian: le
doc-ref: https://git.kernel.org/pub/scm/linux/kernel/git/xiang/erofs-utils.git/tree/include/erofs_fs.h
seq:
  - id: data
    size: 1024
  - id: magic_header
    type: magic_header
  - id: header
    type: header
    size: 128 + magic_header.ext_slots * 16 - magic_header._sizeof
  - id: inode
    type: compact_inode
types:
  magic_header:
    seq:
      - id: magic
        type: u4
        #valid: 3774210530
      - id: crc32
        type: u4
      - id: feature_compat_flags
        type: u4
      - id: block_size_bits
        type: u1
      - id: ext_slots
        type: u1
        doc: superblock size = 128 + sb_extslots * 16
  header:
    seq:
      - id: root_nid
        type: u2
      - id: inos
        type: u8
        doc: total valid ino # (== f_files - f_favail)
      - id: build_time
        type: u8
      - id: build_time_nsec
        type: u4
        doc: inode v1 time derivation in nano scale
      - id: blocks
        type: u4
        doc: used for statfs
      - id: meta_block_address
        type: u4
        doc: start block address of metadata area
      - id: xattr_block_address
        type: u4
        doc: start block address of shared xattr area
      - id: uuid
        size: 16
        doc: 128-bit uuid for volume
      - id: volume_name
        size: 16
      - id: feature_incompat_flags
        type: u4
      - id: some_union
        type: u2
      - id: reserved
        size: 42
  compact_inode:
    # 32-byte reduced form of an ondisk inode
    seq:
      - id: format
        type: u2
      - id: num_xattr
        -orig-id: i_xattr_icount
        type: u2
      - id: mode
        type: u2
      - id: nlink
        type: u2
      - id: inode_size
        type: u4
      - id: reserved1
        type: u4
      - id: some_union
        type: u4
      - id: ino
        type: u4
      - id: uid
        type: u2
      - id: gid
        type: u2
      - id: reserved2
        type: u4
  extended_inode:
    # 64-byte complete form of an ondisk inode
    seq:
      - id: format
        type: u2
      - id: num_xattr
        -orig-id: i_xattr_icount
        type: u2
      - id: mode
        type: u2
      - id: reserved1
        type: u2
      - id: inode_size
        type: u8
      - id: some_union
        type: u4
      - id: ino
        type: u4
      - id: uid
        type: u4
      - id: gid
        type: u4
      - id: ctime
        type: u8
      - id: ctime_nsec
        type: u4
      - id: nlink
        type: u4
      - id: reserved2
        size: 16
  directory:
    seq:
      - id: node_id
        type: u8
      - id: ofs_name
        -orig-id: nameoff
        type: u2
      - id: file_type
        type: u1
        enum: file_types
      - id: reserved
        type: u1
enums:
  file_types:
    0: unknown
    1: regular_file
    2: directory
    3: character_device
    4: block_device
    5: fifo
    6: socket
    7: symlink
  format:
    0: plain
    1: compression_legacy
    2: inline_data
    3: compression
