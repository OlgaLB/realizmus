#!/usr/bin/env python3

import os


def format_history_statistics(dictionary):
    """Output dictionary in specific format: <value key>.

        Parameters:
        ----------
        dictionary : dict
            Dictionary to print in specified format.
    """
    for key in dictionary.keys():
        print(str(dictionary[key]) + ' ' + str(key))


def get_history_statistics():
    """Calculate a count of unique commands that were used in conjunction with sudo.

        Returns:
        ----------
        dict
            Dictionary of unique commands (as keys) and number of their occurrence (as values).
    """
    sudo_history_stats = {}
    if os.path.exists(os.path.expanduser('~/.bash_history')):
        with open(os.path.expanduser('~/.bash_history'), 'r') as history_file:
            for history_record in history_file:
                if history_record.startswith('sudo '):
                    if history_record.rstrip() not in sudo_history_stats.keys():
                        sudo_history_stats[history_record.rstrip()] = 1
                    else:
                        sudo_history_stats[history_record.rstrip()] += 1
    return sudo_history_stats


if __name__ == "__main__":
    format_history_statistics(get_history_statistics())
