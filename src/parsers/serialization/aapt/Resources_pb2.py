# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Resources.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import Configuration_pb2 as Configuration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fResources.proto\x12\x07\x61\x61pt.pb\x1a\x13\x43onfiguration.proto\"\x1a\n\nStringPool\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"<\n\x0eSourcePosition\x12\x13\n\x0bline_number\x18\x01 \x01(\r\x12\x15\n\rcolumn_number\x18\x02 \x01(\r\"E\n\x06Source\x12\x10\n\x08path_idx\x18\x01 \x01(\r\x12)\n\x08position\x18\x02 \x01(\x0b\x32\x17.aapt.pb.SourcePosition\"0\n\x0fToolFingerprint\x12\x0c\n\x04tool\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"\xbb\x01\n\rResourceTable\x12(\n\x0bsource_pool\x18\x01 \x01(\x0b\x32\x13.aapt.pb.StringPool\x12!\n\x07package\x18\x02 \x03(\x0b\x32\x10.aapt.pb.Package\x12)\n\x0boverlayable\x18\x03 \x03(\x0b\x32\x14.aapt.pb.Overlayable\x12\x32\n\x10tool_fingerprint\x18\x04 \x03(\x0b\x32\x18.aapt.pb.ToolFingerprint\"\x17\n\tPackageId\x12\n\n\x02id\x18\x01 \x01(\r\"d\n\x07Package\x12&\n\npackage_id\x18\x01 \x01(\x0b\x32\x12.aapt.pb.PackageId\x12\x14\n\x0cpackage_name\x18\x02 \x01(\t\x12\x1b\n\x04type\x18\x03 \x03(\x0b\x32\r.aapt.pb.Type\"\x14\n\x06TypeId\x12\n\n\x02id\x18\x01 \x01(\r\"U\n\x04Type\x12 \n\x07type_id\x18\x01 \x01(\x0b\x32\x0f.aapt.pb.TypeId\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1d\n\x05\x65ntry\x18\x03 \x03(\x0b\x32\x0e.aapt.pb.Entry\"\xab\x01\n\nVisibility\x12(\n\x05level\x18\x01 \x01(\x0e\x32\x19.aapt.pb.Visibility.Level\x12\x1f\n\x06source\x18\x02 \x01(\x0b\x32\x0f.aapt.pb.Source\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x12\x12\n\nstaged_api\x18\x04 \x01(\x08\"-\n\x05Level\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PRIVATE\x10\x01\x12\n\n\x06PUBLIC\x10\x02\"<\n\x08\x41llowNew\x12\x1f\n\x06source\x18\x01 \x01(\x0b\x32\x0f.aapt.pb.Source\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\"K\n\x0bOverlayable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1f\n\x06source\x18\x02 \x01(\x0b\x32\x0f.aapt.pb.Source\x12\r\n\x05\x61\x63tor\x18\x03 \x01(\t\"\x95\x02\n\x0fOverlayableItem\x12\x1f\n\x06source\x18\x01 \x01(\x0b\x32\x0f.aapt.pb.Source\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12/\n\x06policy\x18\x03 \x03(\x0e\x32\x1f.aapt.pb.OverlayableItem.Policy\x12\x17\n\x0foverlayable_idx\x18\x04 \x01(\r\"\x85\x01\n\x06Policy\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\n\n\x06SYSTEM\x10\x02\x12\n\n\x06VENDOR\x10\x03\x12\x0b\n\x07PRODUCT\x10\x04\x12\r\n\tSIGNATURE\x10\x05\x12\x07\n\x03ODM\x10\x06\x12\x07\n\x03OEM\x10\x07\x12\t\n\x05\x41\x43TOR\x10\x08\x12\x14\n\x10\x43ONFIG_SIGNATURE\x10\t\">\n\x08StagedId\x12\x1f\n\x06source\x18\x01 \x01(\x0b\x32\x0f.aapt.pb.Source\x12\x11\n\tstaged_id\x18\x02 \x01(\r\"\x15\n\x07\x45ntryId\x12\n\n\x02id\x18\x01 \x01(\r\"\x8e\x02\n\x05\x45ntry\x12\"\n\x08\x65ntry_id\x18\x01 \x01(\x0b\x32\x10.aapt.pb.EntryId\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\'\n\nvisibility\x18\x03 \x01(\x0b\x32\x13.aapt.pb.Visibility\x12$\n\tallow_new\x18\x04 \x01(\x0b\x32\x11.aapt.pb.AllowNew\x12\x32\n\x10overlayable_item\x18\x05 \x01(\x0b\x32\x18.aapt.pb.OverlayableItem\x12*\n\x0c\x63onfig_value\x18\x06 \x03(\x0b\x32\x14.aapt.pb.ConfigValue\x12$\n\tstaged_id\x18\x07 \x01(\x0b\x32\x11.aapt.pb.StagedId\"T\n\x0b\x43onfigValue\x12&\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x16.aapt.pb.Configuration\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.aapt.pb.Value\"\xa1\x01\n\x05Value\x12\x1f\n\x06source\x18\x01 \x01(\x0b\x32\x0f.aapt.pb.Source\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12\x0c\n\x04weak\x18\x03 \x01(\x08\x12\x1d\n\x04item\x18\x04 \x01(\x0b\x32\r.aapt.pb.ItemH\x00\x12\x30\n\x0e\x63ompound_value\x18\x05 \x01(\x0b\x32\x16.aapt.pb.CompoundValueH\x00\x42\x07\n\x05value\"\x8d\x02\n\x04Item\x12!\n\x03ref\x18\x01 \x01(\x0b\x32\x12.aapt.pb.ReferenceH\x00\x12\x1e\n\x03str\x18\x02 \x01(\x0b\x32\x0f.aapt.pb.StringH\x00\x12%\n\x07raw_str\x18\x03 \x01(\x0b\x32\x12.aapt.pb.RawStringH\x00\x12+\n\nstyled_str\x18\x04 \x01(\x0b\x32\x15.aapt.pb.StyledStringH\x00\x12&\n\x04\x66ile\x18\x05 \x01(\x0b\x32\x16.aapt.pb.FileReferenceH\x00\x12\x19\n\x02id\x18\x06 \x01(\x0b\x32\x0b.aapt.pb.IdH\x00\x12\"\n\x04prim\x18\x07 \x01(\x0b\x32\x12.aapt.pb.PrimitiveH\x00\x42\x07\n\x05value\"\xef\x01\n\rCompoundValue\x12\"\n\x04\x61ttr\x18\x01 \x01(\x0b\x32\x12.aapt.pb.AttributeH\x00\x12\x1f\n\x05style\x18\x02 \x01(\x0b\x32\x0e.aapt.pb.StyleH\x00\x12\'\n\tstyleable\x18\x03 \x01(\x0b\x32\x12.aapt.pb.StyleableH\x00\x12\x1f\n\x05\x61rray\x18\x04 \x01(\x0b\x32\x0e.aapt.pb.ArrayH\x00\x12!\n\x06plural\x18\x05 \x01(\x0b\x32\x0f.aapt.pb.PluralH\x00\x12#\n\x05macro\x18\x06 \x01(\x0b\x32\x12.aapt.pb.MacroBodyH\x00\x42\x07\n\x05value\"\x18\n\x07\x42oolean\x12\r\n\x05value\x18\x01 \x01(\x08\"\xd0\x01\n\tReference\x12%\n\x04type\x18\x01 \x01(\x0e\x32\x17.aapt.pb.Reference.Type\x12\n\n\x02id\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07private\x18\x04 \x01(\x08\x12$\n\nis_dynamic\x18\x05 \x01(\x0b\x32\x10.aapt.pb.Boolean\x12\x12\n\ntype_flags\x18\x06 \x01(\r\x12\x11\n\tallow_raw\x18\x07 \x01(\x08\"$\n\x04Type\x12\r\n\tREFERENCE\x10\x00\x12\r\n\tATTRIBUTE\x10\x01\"\x04\n\x02Id\"\x17\n\x06String\x12\r\n\x05value\x18\x01 \x01(\t\"\x1a\n\tRawString\x12\r\n\x05value\x18\x01 \x01(\t\"\x83\x01\n\x0cStyledString\x12\r\n\x05value\x18\x01 \x01(\t\x12(\n\x04span\x18\x02 \x03(\x0b\x32\x1a.aapt.pb.StyledString.Span\x1a:\n\x04Span\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x12\n\nfirst_char\x18\x02 \x01(\r\x12\x11\n\tlast_char\x18\x03 \x01(\r\"\x85\x01\n\rFileReference\x12\x0c\n\x04path\x18\x01 \x01(\t\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.aapt.pb.FileReference.Type\";\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03PNG\x10\x01\x12\x0e\n\nBINARY_XML\x10\x02\x12\r\n\tPROTO_XML\x10\x03\"\x83\x04\n\tPrimitive\x12\x31\n\nnull_value\x18\x01 \x01(\x0b\x32\x1b.aapt.pb.Primitive.NullTypeH\x00\x12\x33\n\x0b\x65mpty_value\x18\x02 \x01(\x0b\x32\x1c.aapt.pb.Primitive.EmptyTypeH\x00\x12\x15\n\x0b\x66loat_value\x18\x03 \x01(\x02H\x00\x12\x19\n\x0f\x64imension_value\x18\r \x01(\rH\x00\x12\x18\n\x0e\x66raction_value\x18\x0e \x01(\rH\x00\x12\x1b\n\x11int_decimal_value\x18\x06 \x01(\x05H\x00\x12\x1f\n\x15int_hexadecimal_value\x18\x07 \x01(\rH\x00\x12\x17\n\rboolean_value\x18\x08 \x01(\x08H\x00\x12\x1b\n\x11\x63olor_argb8_value\x18\t \x01(\rH\x00\x12\x1a\n\x10\x63olor_rgb8_value\x18\n \x01(\rH\x00\x12\x1b\n\x11\x63olor_argb4_value\x18\x0b \x01(\rH\x00\x12\x1a\n\x10\x63olor_rgb4_value\x18\x0c \x01(\rH\x00\x12(\n\x1a\x64imension_value_deprecated\x18\x04 \x01(\x02\x42\x02\x18\x01H\x00\x12\'\n\x19\x66raction_value_deprecated\x18\x05 \x01(\x02\x42\x02\x18\x01H\x00\x1a\n\n\x08NullType\x1a\x0b\n\tEmptyTypeB\r\n\x0boneof_value\"\x90\x03\n\tAttribute\x12\x14\n\x0c\x66ormat_flags\x18\x01 \x01(\r\x12\x0f\n\x07min_int\x18\x02 \x01(\x05\x12\x0f\n\x07max_int\x18\x03 \x01(\x05\x12)\n\x06symbol\x18\x04 \x03(\x0b\x32\x19.aapt.pb.Attribute.Symbol\x1ay\n\x06Symbol\x12\x1f\n\x06source\x18\x01 \x01(\x0b\x32\x0f.aapt.pb.Source\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12 \n\x04name\x18\x03 \x01(\x0b\x32\x12.aapt.pb.Reference\x12\r\n\x05value\x18\x04 \x01(\r\x12\x0c\n\x04type\x18\x05 \x01(\r\"\xa4\x01\n\x0b\x46ormatFlags\x12\x08\n\x04NONE\x10\x00\x12\t\n\x03\x41NY\x10\xff\xff\x03\x12\r\n\tREFERENCE\x10\x01\x12\n\n\x06STRING\x10\x02\x12\x0b\n\x07INTEGER\x10\x04\x12\x0b\n\x07\x42OOLEAN\x10\x08\x12\t\n\x05\x43OLOR\x10\x10\x12\t\n\x05\x46LOAT\x10 \x12\r\n\tDIMENSION\x10@\x12\r\n\x08\x46RACTION\x10\x80\x01\x12\n\n\x04\x45NUM\x10\x80\x80\x04\x12\x0b\n\x05\x46LAGS\x10\x80\x80\x08\"\xf1\x01\n\x05Style\x12\"\n\x06parent\x18\x01 \x01(\x0b\x32\x12.aapt.pb.Reference\x12&\n\rparent_source\x18\x02 \x01(\x0b\x32\x0f.aapt.pb.Source\x12#\n\x05\x65ntry\x18\x03 \x03(\x0b\x32\x14.aapt.pb.Style.Entry\x1aw\n\x05\x45ntry\x12\x1f\n\x06source\x18\x01 \x01(\x0b\x32\x0f.aapt.pb.Source\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12\x1f\n\x03key\x18\x03 \x01(\x0b\x32\x12.aapt.pb.Reference\x12\x1b\n\x04item\x18\x04 \x01(\x0b\x32\r.aapt.pb.Item\"\x91\x01\n\tStyleable\x12\'\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x18.aapt.pb.Styleable.Entry\x1a[\n\x05\x45ntry\x12\x1f\n\x06source\x18\x01 \x01(\x0b\x32\x0f.aapt.pb.Source\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12 \n\x04\x61ttr\x18\x03 \x01(\x0b\x32\x12.aapt.pb.Reference\"\x8a\x01\n\x05\x41rray\x12\'\n\x07\x65lement\x18\x01 \x03(\x0b\x32\x16.aapt.pb.Array.Element\x1aX\n\x07\x45lement\x12\x1f\n\x06source\x18\x01 \x01(\x0b\x32\x0f.aapt.pb.Source\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12\x1b\n\x04item\x18\x03 \x01(\x0b\x32\r.aapt.pb.Item\"\xef\x01\n\x06Plural\x12$\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x15.aapt.pb.Plural.Entry\x1a|\n\x05\x45ntry\x12\x1f\n\x06source\x18\x01 \x01(\x0b\x32\x0f.aapt.pb.Source\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12$\n\x05\x61rity\x18\x03 \x01(\x0e\x32\x15.aapt.pb.Plural.Arity\x12\x1b\n\x04item\x18\x04 \x01(\x0b\x32\r.aapt.pb.Item\"A\n\x05\x41rity\x12\x08\n\x04ZERO\x10\x00\x12\x07\n\x03ONE\x10\x01\x12\x07\n\x03TWO\x10\x02\x12\x07\n\x03\x46\x45W\x10\x03\x12\x08\n\x04MANY\x10\x04\x12\t\n\x05OTHER\x10\x05\"r\n\x07XmlNode\x12&\n\x07\x65lement\x18\x01 \x01(\x0b\x32\x13.aapt.pb.XmlElementH\x00\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12\'\n\x06source\x18\x03 \x01(\x0b\x32\x17.aapt.pb.SourcePositionB\x06\n\x04node\"\xb2\x01\n\nXmlElement\x12\x34\n\x15namespace_declaration\x18\x01 \x03(\x0b\x32\x15.aapt.pb.XmlNamespace\x12\x15\n\rnamespace_uri\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12(\n\tattribute\x18\x04 \x03(\x0b\x32\x15.aapt.pb.XmlAttribute\x12\x1f\n\x05\x63hild\x18\x05 \x03(\x0b\x32\x10.aapt.pb.XmlNode\"T\n\x0cXmlNamespace\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\'\n\x06source\x18\x03 \x01(\x0b\x32\x17.aapt.pb.SourcePosition\"\xa6\x01\n\x0cXmlAttribute\x12\x15\n\rnamespace_uri\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\'\n\x06source\x18\x04 \x01(\x0b\x32\x17.aapt.pb.SourcePosition\x12\x13\n\x0bresource_id\x18\x05 \x01(\r\x12$\n\rcompiled_item\x18\x06 \x01(\x0b\x32\r.aapt.pb.Item\"\xe7\x01\n\tMacroBody\x12\x12\n\nraw_string\x18\x01 \x01(\t\x12*\n\x0cstyle_string\x18\x02 \x01(\x0b\x32\x14.aapt.pb.StyleString\x12?\n\x17untranslatable_sections\x18\x03 \x03(\x0b\x32\x1e.aapt.pb.UntranslatableSection\x12\x30\n\x0fnamespace_stack\x18\x04 \x03(\x0b\x32\x17.aapt.pb.NamespaceAlias\x12\'\n\x06source\x18\x05 \x01(\x0b\x32\x17.aapt.pb.SourcePosition\"J\n\x0eNamespaceAlias\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x14\n\x0cpackage_name\x18\x02 \x01(\t\x12\x12\n\nis_private\x18\x03 \x01(\x08\"\x82\x01\n\x0bStyleString\x12\x0b\n\x03str\x18\x01 \x01(\t\x12(\n\x05spans\x18\x02 \x03(\x0b\x32\x19.aapt.pb.StyleString.Span\x1a<\n\x04Span\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bstart_index\x18\x02 \x01(\r\x12\x11\n\tend_index\x18\x03 \x01(\r\"?\n\x15UntranslatableSection\x12\x13\n\x0bstart_index\x18\x01 \x01(\x04\x12\x11\n\tend_index\x18\x02 \x01(\x04\x42\x12\n\x10\x63om.android.aaptb\x06proto3')



_STRINGPOOL = DESCRIPTOR.message_types_by_name['StringPool']
_SOURCEPOSITION = DESCRIPTOR.message_types_by_name['SourcePosition']
_SOURCE = DESCRIPTOR.message_types_by_name['Source']
_TOOLFINGERPRINT = DESCRIPTOR.message_types_by_name['ToolFingerprint']
_RESOURCETABLE = DESCRIPTOR.message_types_by_name['ResourceTable']
_PACKAGEID = DESCRIPTOR.message_types_by_name['PackageId']
_PACKAGE = DESCRIPTOR.message_types_by_name['Package']
_TYPEID = DESCRIPTOR.message_types_by_name['TypeId']
_TYPE = DESCRIPTOR.message_types_by_name['Type']
_VISIBILITY = DESCRIPTOR.message_types_by_name['Visibility']
_ALLOWNEW = DESCRIPTOR.message_types_by_name['AllowNew']
_OVERLAYABLE = DESCRIPTOR.message_types_by_name['Overlayable']
_OVERLAYABLEITEM = DESCRIPTOR.message_types_by_name['OverlayableItem']
_STAGEDID = DESCRIPTOR.message_types_by_name['StagedId']
_ENTRYID = DESCRIPTOR.message_types_by_name['EntryId']
_ENTRY = DESCRIPTOR.message_types_by_name['Entry']
_CONFIGVALUE = DESCRIPTOR.message_types_by_name['ConfigValue']
_VALUE = DESCRIPTOR.message_types_by_name['Value']
_ITEM = DESCRIPTOR.message_types_by_name['Item']
_COMPOUNDVALUE = DESCRIPTOR.message_types_by_name['CompoundValue']
_BOOLEAN = DESCRIPTOR.message_types_by_name['Boolean']
_REFERENCE = DESCRIPTOR.message_types_by_name['Reference']
_ID = DESCRIPTOR.message_types_by_name['Id']
_STRING = DESCRIPTOR.message_types_by_name['String']
_RAWSTRING = DESCRIPTOR.message_types_by_name['RawString']
_STYLEDSTRING = DESCRIPTOR.message_types_by_name['StyledString']
_STYLEDSTRING_SPAN = _STYLEDSTRING.nested_types_by_name['Span']
_FILEREFERENCE = DESCRIPTOR.message_types_by_name['FileReference']
_PRIMITIVE = DESCRIPTOR.message_types_by_name['Primitive']
_PRIMITIVE_NULLTYPE = _PRIMITIVE.nested_types_by_name['NullType']
_PRIMITIVE_EMPTYTYPE = _PRIMITIVE.nested_types_by_name['EmptyType']
_ATTRIBUTE = DESCRIPTOR.message_types_by_name['Attribute']
_ATTRIBUTE_SYMBOL = _ATTRIBUTE.nested_types_by_name['Symbol']
_STYLE = DESCRIPTOR.message_types_by_name['Style']
_STYLE_ENTRY = _STYLE.nested_types_by_name['Entry']
_STYLEABLE = DESCRIPTOR.message_types_by_name['Styleable']
_STYLEABLE_ENTRY = _STYLEABLE.nested_types_by_name['Entry']
_ARRAY = DESCRIPTOR.message_types_by_name['Array']
_ARRAY_ELEMENT = _ARRAY.nested_types_by_name['Element']
_PLURAL = DESCRIPTOR.message_types_by_name['Plural']
_PLURAL_ENTRY = _PLURAL.nested_types_by_name['Entry']
_XMLNODE = DESCRIPTOR.message_types_by_name['XmlNode']
_XMLELEMENT = DESCRIPTOR.message_types_by_name['XmlElement']
_XMLNAMESPACE = DESCRIPTOR.message_types_by_name['XmlNamespace']
_XMLATTRIBUTE = DESCRIPTOR.message_types_by_name['XmlAttribute']
_MACROBODY = DESCRIPTOR.message_types_by_name['MacroBody']
_NAMESPACEALIAS = DESCRIPTOR.message_types_by_name['NamespaceAlias']
_STYLESTRING = DESCRIPTOR.message_types_by_name['StyleString']
_STYLESTRING_SPAN = _STYLESTRING.nested_types_by_name['Span']
_UNTRANSLATABLESECTION = DESCRIPTOR.message_types_by_name['UntranslatableSection']
_VISIBILITY_LEVEL = _VISIBILITY.enum_types_by_name['Level']
_OVERLAYABLEITEM_POLICY = _OVERLAYABLEITEM.enum_types_by_name['Policy']
_REFERENCE_TYPE = _REFERENCE.enum_types_by_name['Type']
_FILEREFERENCE_TYPE = _FILEREFERENCE.enum_types_by_name['Type']
_ATTRIBUTE_FORMATFLAGS = _ATTRIBUTE.enum_types_by_name['FormatFlags']
_PLURAL_ARITY = _PLURAL.enum_types_by_name['Arity']
StringPool = _reflection.GeneratedProtocolMessageType('StringPool', (_message.Message,), {
  'DESCRIPTOR' : _STRINGPOOL,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.StringPool)
  })
_sym_db.RegisterMessage(StringPool)

SourcePosition = _reflection.GeneratedProtocolMessageType('SourcePosition', (_message.Message,), {
  'DESCRIPTOR' : _SOURCEPOSITION,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.SourcePosition)
  })
_sym_db.RegisterMessage(SourcePosition)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), {
  'DESCRIPTOR' : _SOURCE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Source)
  })
_sym_db.RegisterMessage(Source)

ToolFingerprint = _reflection.GeneratedProtocolMessageType('ToolFingerprint', (_message.Message,), {
  'DESCRIPTOR' : _TOOLFINGERPRINT,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.ToolFingerprint)
  })
_sym_db.RegisterMessage(ToolFingerprint)

ResourceTable = _reflection.GeneratedProtocolMessageType('ResourceTable', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCETABLE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.ResourceTable)
  })
_sym_db.RegisterMessage(ResourceTable)

PackageId = _reflection.GeneratedProtocolMessageType('PackageId', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGEID,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.PackageId)
  })
_sym_db.RegisterMessage(PackageId)

Package = _reflection.GeneratedProtocolMessageType('Package', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Package)
  })
_sym_db.RegisterMessage(Package)

TypeId = _reflection.GeneratedProtocolMessageType('TypeId', (_message.Message,), {
  'DESCRIPTOR' : _TYPEID,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.TypeId)
  })
_sym_db.RegisterMessage(TypeId)

Type = _reflection.GeneratedProtocolMessageType('Type', (_message.Message,), {
  'DESCRIPTOR' : _TYPE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Type)
  })
_sym_db.RegisterMessage(Type)

Visibility = _reflection.GeneratedProtocolMessageType('Visibility', (_message.Message,), {
  'DESCRIPTOR' : _VISIBILITY,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Visibility)
  })
_sym_db.RegisterMessage(Visibility)

AllowNew = _reflection.GeneratedProtocolMessageType('AllowNew', (_message.Message,), {
  'DESCRIPTOR' : _ALLOWNEW,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.AllowNew)
  })
_sym_db.RegisterMessage(AllowNew)

Overlayable = _reflection.GeneratedProtocolMessageType('Overlayable', (_message.Message,), {
  'DESCRIPTOR' : _OVERLAYABLE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Overlayable)
  })
_sym_db.RegisterMessage(Overlayable)

OverlayableItem = _reflection.GeneratedProtocolMessageType('OverlayableItem', (_message.Message,), {
  'DESCRIPTOR' : _OVERLAYABLEITEM,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.OverlayableItem)
  })
_sym_db.RegisterMessage(OverlayableItem)

StagedId = _reflection.GeneratedProtocolMessageType('StagedId', (_message.Message,), {
  'DESCRIPTOR' : _STAGEDID,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.StagedId)
  })
_sym_db.RegisterMessage(StagedId)

EntryId = _reflection.GeneratedProtocolMessageType('EntryId', (_message.Message,), {
  'DESCRIPTOR' : _ENTRYID,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.EntryId)
  })
_sym_db.RegisterMessage(EntryId)

Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
  'DESCRIPTOR' : _ENTRY,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Entry)
  })
_sym_db.RegisterMessage(Entry)

ConfigValue = _reflection.GeneratedProtocolMessageType('ConfigValue', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGVALUE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.ConfigValue)
  })
_sym_db.RegisterMessage(ConfigValue)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Value)
  })
_sym_db.RegisterMessage(Value)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Item)
  })
_sym_db.RegisterMessage(Item)

CompoundValue = _reflection.GeneratedProtocolMessageType('CompoundValue', (_message.Message,), {
  'DESCRIPTOR' : _COMPOUNDVALUE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.CompoundValue)
  })
_sym_db.RegisterMessage(CompoundValue)

Boolean = _reflection.GeneratedProtocolMessageType('Boolean', (_message.Message,), {
  'DESCRIPTOR' : _BOOLEAN,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Boolean)
  })
_sym_db.RegisterMessage(Boolean)

Reference = _reflection.GeneratedProtocolMessageType('Reference', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Reference)
  })
_sym_db.RegisterMessage(Reference)

Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), {
  'DESCRIPTOR' : _ID,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Id)
  })
_sym_db.RegisterMessage(Id)

String = _reflection.GeneratedProtocolMessageType('String', (_message.Message,), {
  'DESCRIPTOR' : _STRING,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.String)
  })
_sym_db.RegisterMessage(String)

RawString = _reflection.GeneratedProtocolMessageType('RawString', (_message.Message,), {
  'DESCRIPTOR' : _RAWSTRING,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.RawString)
  })
_sym_db.RegisterMessage(RawString)

StyledString = _reflection.GeneratedProtocolMessageType('StyledString', (_message.Message,), {

  'Span' : _reflection.GeneratedProtocolMessageType('Span', (_message.Message,), {
    'DESCRIPTOR' : _STYLEDSTRING_SPAN,
    '__module__' : 'Resources_pb2'
    # @@protoc_insertion_point(class_scope:aapt.pb.StyledString.Span)
    })
  ,
  'DESCRIPTOR' : _STYLEDSTRING,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.StyledString)
  })
_sym_db.RegisterMessage(StyledString)
_sym_db.RegisterMessage(StyledString.Span)

FileReference = _reflection.GeneratedProtocolMessageType('FileReference', (_message.Message,), {
  'DESCRIPTOR' : _FILEREFERENCE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.FileReference)
  })
_sym_db.RegisterMessage(FileReference)

Primitive = _reflection.GeneratedProtocolMessageType('Primitive', (_message.Message,), {

  'NullType' : _reflection.GeneratedProtocolMessageType('NullType', (_message.Message,), {
    'DESCRIPTOR' : _PRIMITIVE_NULLTYPE,
    '__module__' : 'Resources_pb2'
    # @@protoc_insertion_point(class_scope:aapt.pb.Primitive.NullType)
    })
  ,

  'EmptyType' : _reflection.GeneratedProtocolMessageType('EmptyType', (_message.Message,), {
    'DESCRIPTOR' : _PRIMITIVE_EMPTYTYPE,
    '__module__' : 'Resources_pb2'
    # @@protoc_insertion_point(class_scope:aapt.pb.Primitive.EmptyType)
    })
  ,
  'DESCRIPTOR' : _PRIMITIVE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Primitive)
  })
_sym_db.RegisterMessage(Primitive)
_sym_db.RegisterMessage(Primitive.NullType)
_sym_db.RegisterMessage(Primitive.EmptyType)

Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), {

  'Symbol' : _reflection.GeneratedProtocolMessageType('Symbol', (_message.Message,), {
    'DESCRIPTOR' : _ATTRIBUTE_SYMBOL,
    '__module__' : 'Resources_pb2'
    # @@protoc_insertion_point(class_scope:aapt.pb.Attribute.Symbol)
    })
  ,
  'DESCRIPTOR' : _ATTRIBUTE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Attribute)
  })
_sym_db.RegisterMessage(Attribute)
_sym_db.RegisterMessage(Attribute.Symbol)

Style = _reflection.GeneratedProtocolMessageType('Style', (_message.Message,), {

  'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
    'DESCRIPTOR' : _STYLE_ENTRY,
    '__module__' : 'Resources_pb2'
    # @@protoc_insertion_point(class_scope:aapt.pb.Style.Entry)
    })
  ,
  'DESCRIPTOR' : _STYLE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Style)
  })
_sym_db.RegisterMessage(Style)
_sym_db.RegisterMessage(Style.Entry)

Styleable = _reflection.GeneratedProtocolMessageType('Styleable', (_message.Message,), {

  'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
    'DESCRIPTOR' : _STYLEABLE_ENTRY,
    '__module__' : 'Resources_pb2'
    # @@protoc_insertion_point(class_scope:aapt.pb.Styleable.Entry)
    })
  ,
  'DESCRIPTOR' : _STYLEABLE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Styleable)
  })
_sym_db.RegisterMessage(Styleable)
_sym_db.RegisterMessage(Styleable.Entry)

Array = _reflection.GeneratedProtocolMessageType('Array', (_message.Message,), {

  'Element' : _reflection.GeneratedProtocolMessageType('Element', (_message.Message,), {
    'DESCRIPTOR' : _ARRAY_ELEMENT,
    '__module__' : 'Resources_pb2'
    # @@protoc_insertion_point(class_scope:aapt.pb.Array.Element)
    })
  ,
  'DESCRIPTOR' : _ARRAY,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Array)
  })
_sym_db.RegisterMessage(Array)
_sym_db.RegisterMessage(Array.Element)

Plural = _reflection.GeneratedProtocolMessageType('Plural', (_message.Message,), {

  'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
    'DESCRIPTOR' : _PLURAL_ENTRY,
    '__module__' : 'Resources_pb2'
    # @@protoc_insertion_point(class_scope:aapt.pb.Plural.Entry)
    })
  ,
  'DESCRIPTOR' : _PLURAL,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.Plural)
  })
_sym_db.RegisterMessage(Plural)
_sym_db.RegisterMessage(Plural.Entry)

XmlNode = _reflection.GeneratedProtocolMessageType('XmlNode', (_message.Message,), {
  'DESCRIPTOR' : _XMLNODE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.XmlNode)
  })
_sym_db.RegisterMessage(XmlNode)

XmlElement = _reflection.GeneratedProtocolMessageType('XmlElement', (_message.Message,), {
  'DESCRIPTOR' : _XMLELEMENT,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.XmlElement)
  })
_sym_db.RegisterMessage(XmlElement)

XmlNamespace = _reflection.GeneratedProtocolMessageType('XmlNamespace', (_message.Message,), {
  'DESCRIPTOR' : _XMLNAMESPACE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.XmlNamespace)
  })
_sym_db.RegisterMessage(XmlNamespace)

XmlAttribute = _reflection.GeneratedProtocolMessageType('XmlAttribute', (_message.Message,), {
  'DESCRIPTOR' : _XMLATTRIBUTE,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.XmlAttribute)
  })
_sym_db.RegisterMessage(XmlAttribute)

MacroBody = _reflection.GeneratedProtocolMessageType('MacroBody', (_message.Message,), {
  'DESCRIPTOR' : _MACROBODY,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.MacroBody)
  })
_sym_db.RegisterMessage(MacroBody)

NamespaceAlias = _reflection.GeneratedProtocolMessageType('NamespaceAlias', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACEALIAS,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.NamespaceAlias)
  })
_sym_db.RegisterMessage(NamespaceAlias)

StyleString = _reflection.GeneratedProtocolMessageType('StyleString', (_message.Message,), {

  'Span' : _reflection.GeneratedProtocolMessageType('Span', (_message.Message,), {
    'DESCRIPTOR' : _STYLESTRING_SPAN,
    '__module__' : 'Resources_pb2'
    # @@protoc_insertion_point(class_scope:aapt.pb.StyleString.Span)
    })
  ,
  'DESCRIPTOR' : _STYLESTRING,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.StyleString)
  })
_sym_db.RegisterMessage(StyleString)
_sym_db.RegisterMessage(StyleString.Span)

UntranslatableSection = _reflection.GeneratedProtocolMessageType('UntranslatableSection', (_message.Message,), {
  'DESCRIPTOR' : _UNTRANSLATABLESECTION,
  '__module__' : 'Resources_pb2'
  # @@protoc_insertion_point(class_scope:aapt.pb.UntranslatableSection)
  })
_sym_db.RegisterMessage(UntranslatableSection)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.android.aapt'
  _PRIMITIVE.fields_by_name['dimension_value_deprecated']._options = None
  _PRIMITIVE.fields_by_name['dimension_value_deprecated']._serialized_options = b'\030\001'
  _PRIMITIVE.fields_by_name['fraction_value_deprecated']._options = None
  _PRIMITIVE.fields_by_name['fraction_value_deprecated']._serialized_options = b'\030\001'
  _STRINGPOOL._serialized_start=49
  _STRINGPOOL._serialized_end=75
  _SOURCEPOSITION._serialized_start=77
  _SOURCEPOSITION._serialized_end=137
  _SOURCE._serialized_start=139
  _SOURCE._serialized_end=208
  _TOOLFINGERPRINT._serialized_start=210
  _TOOLFINGERPRINT._serialized_end=258
  _RESOURCETABLE._serialized_start=261
  _RESOURCETABLE._serialized_end=448
  _PACKAGEID._serialized_start=450
  _PACKAGEID._serialized_end=473
  _PACKAGE._serialized_start=475
  _PACKAGE._serialized_end=575
  _TYPEID._serialized_start=577
  _TYPEID._serialized_end=597
  _TYPE._serialized_start=599
  _TYPE._serialized_end=684
  _VISIBILITY._serialized_start=687
  _VISIBILITY._serialized_end=858
  _VISIBILITY_LEVEL._serialized_start=813
  _VISIBILITY_LEVEL._serialized_end=858
  _ALLOWNEW._serialized_start=860
  _ALLOWNEW._serialized_end=920
  _OVERLAYABLE._serialized_start=922
  _OVERLAYABLE._serialized_end=997
  _OVERLAYABLEITEM._serialized_start=1000
  _OVERLAYABLEITEM._serialized_end=1277
  _OVERLAYABLEITEM_POLICY._serialized_start=1144
  _OVERLAYABLEITEM_POLICY._serialized_end=1277
  _STAGEDID._serialized_start=1279
  _STAGEDID._serialized_end=1341
  _ENTRYID._serialized_start=1343
  _ENTRYID._serialized_end=1364
  _ENTRY._serialized_start=1367
  _ENTRY._serialized_end=1637
  _CONFIGVALUE._serialized_start=1639
  _CONFIGVALUE._serialized_end=1723
  _VALUE._serialized_start=1726
  _VALUE._serialized_end=1887
  _ITEM._serialized_start=1890
  _ITEM._serialized_end=2159
  _COMPOUNDVALUE._serialized_start=2162
  _COMPOUNDVALUE._serialized_end=2401
  _BOOLEAN._serialized_start=2403
  _BOOLEAN._serialized_end=2427
  _REFERENCE._serialized_start=2430
  _REFERENCE._serialized_end=2638
  _REFERENCE_TYPE._serialized_start=2602
  _REFERENCE_TYPE._serialized_end=2638
  _ID._serialized_start=2640
  _ID._serialized_end=2644
  _STRING._serialized_start=2646
  _STRING._serialized_end=2669
  _RAWSTRING._serialized_start=2671
  _RAWSTRING._serialized_end=2697
  _STYLEDSTRING._serialized_start=2700
  _STYLEDSTRING._serialized_end=2831
  _STYLEDSTRING_SPAN._serialized_start=2773
  _STYLEDSTRING_SPAN._serialized_end=2831
  _FILEREFERENCE._serialized_start=2834
  _FILEREFERENCE._serialized_end=2967
  _FILEREFERENCE_TYPE._serialized_start=2908
  _FILEREFERENCE_TYPE._serialized_end=2967
  _PRIMITIVE._serialized_start=2970
  _PRIMITIVE._serialized_end=3485
  _PRIMITIVE_NULLTYPE._serialized_start=3447
  _PRIMITIVE_NULLTYPE._serialized_end=3457
  _PRIMITIVE_EMPTYTYPE._serialized_start=3459
  _PRIMITIVE_EMPTYTYPE._serialized_end=3470
  _ATTRIBUTE._serialized_start=3488
  _ATTRIBUTE._serialized_end=3888
  _ATTRIBUTE_SYMBOL._serialized_start=3600
  _ATTRIBUTE_SYMBOL._serialized_end=3721
  _ATTRIBUTE_FORMATFLAGS._serialized_start=3724
  _ATTRIBUTE_FORMATFLAGS._serialized_end=3888
  _STYLE._serialized_start=3891
  _STYLE._serialized_end=4132
  _STYLE_ENTRY._serialized_start=4013
  _STYLE_ENTRY._serialized_end=4132
  _STYLEABLE._serialized_start=4135
  _STYLEABLE._serialized_end=4280
  _STYLEABLE_ENTRY._serialized_start=4189
  _STYLEABLE_ENTRY._serialized_end=4280
  _ARRAY._serialized_start=4283
  _ARRAY._serialized_end=4421
  _ARRAY_ELEMENT._serialized_start=4333
  _ARRAY_ELEMENT._serialized_end=4421
  _PLURAL._serialized_start=4424
  _PLURAL._serialized_end=4663
  _PLURAL_ENTRY._serialized_start=4472
  _PLURAL_ENTRY._serialized_end=4596
  _PLURAL_ARITY._serialized_start=4598
  _PLURAL_ARITY._serialized_end=4663
  _XMLNODE._serialized_start=4665
  _XMLNODE._serialized_end=4779
  _XMLELEMENT._serialized_start=4782
  _XMLELEMENT._serialized_end=4960
  _XMLNAMESPACE._serialized_start=4962
  _XMLNAMESPACE._serialized_end=5046
  _XMLATTRIBUTE._serialized_start=5049
  _XMLATTRIBUTE._serialized_end=5215
  _MACROBODY._serialized_start=5218
  _MACROBODY._serialized_end=5449
  _NAMESPACEALIAS._serialized_start=5451
  _NAMESPACEALIAS._serialized_end=5525
  _STYLESTRING._serialized_start=5528
  _STYLESTRING._serialized_end=5658
  _STYLESTRING_SPAN._serialized_start=5598
  _STYLESTRING_SPAN._serialized_end=5658
  _UNTRANSLATABLESECTION._serialized_start=5660
  _UNTRANSLATABLESECTION._serialized_end=5723
# @@protoc_insertion_point(module_scope)
