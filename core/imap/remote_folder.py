import re
import utils


class RemoteFolder:

    def __init__(self, folder_meta: str, remote_login):
        self._flags = list()

        flags_and_name = folder_meta.split(' "/" ')

        match_expression = r"\((\\.*)\)"
        match = re.match(match_expression, flags_and_name[0])
        if match is None:
            raise ValueError(f"Invalid folder metadata: {folder_meta}")

        flag_list = match.group(1).split(' ')
        for flag in flag_list:
            self._flags.append(flag)

        # GMail sends folder names in a quote
        self._name = utils.unquote_string(flags_and_name[1])

    def get_name(self) -> str:
        return self._name

    def is_junk_folder(self) -> bool:
        return self._has_flag("\\Junk")

    def has_children(self) -> bool:
        return self._has_flag("\\HasChildren")

    def has_no_children(self) -> bool:
        return self._has_flag("\\HasNoChildren")

    def _has_flag(self, flag_name):
        return flag_name in self._flags
