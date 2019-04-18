import imaplib
import logging
from core.imap.remote_folder import RemoteFolder
from typing import List


class Connection:
    _remote_login = None

    _remote_folders: List[RemoteFolder] = None
    _remote_folders_tree: dict = None

    def __init__(self, remote_login: str, remote_pass: str, remote_url: str):

        _imap_login = imaplib.IMAP4_SSL(remote_url)
        try:
            _imap_login.login(remote_login, remote_pass)
        except imaplib.IMAP4.error as err:
            logging.error("Login failed for %s@%s", remote_login, remote_url)
            raise err

        self._remote_login = _imap_login

    def get_remote_folders(self) -> List[RemoteFolder]:
        self._assert_connected()

        if self._remote_folders is None:
            remote_folder_list = []
            for remote_folder in self._remote_login.list()[1]:
                folder_meta = remote_folder.decode()
                folder = RemoteFolder(folder_meta, self._remote_login)
                remote_folder_list.append(folder)

            self._remote_folders = remote_folder_list

        return self._remote_folders

    def get_remote_folders_tree(self) -> dict:
        self._assert_connected()

        if self._remote_folders_tree is None:
            tree = dict()
            all_parent_nodes = list()
            remote_folders = self.get_remote_folders()

            for remote_folder in remote_folders:
                _spl = remote_folder.get_name().split('/')
                _has_children = remote_folder.has_children()

                if _has_children:
                    all_parent_nodes.append(remote_folder.get_name())

                if not remote_folder.get_name() in tree:
                    if not _has_children and _spl[0] in all_parent_nodes:
                        tree[_spl[0]].append(_spl[1])
                    else:
                        tree[remote_folder.get_name()] = list()

            self._remote_folders_tree = tree

        return self._remote_folders_tree

    def _assert_connected(self):
        if self._remote_login is None:
            raise ValueError("Not connected to the remote IMAP server")
