#!/usr/bin/python
# locustor: Tool to execute locust and produce reports
#
# Copyright (C) 2017 jamatute <jmm@riseup.net>
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from locustor.cli_arguments import load_logger, load_parser, load_config


def main():
    parser = load_parser()
    args = parser.parse_args()
    log = load_logger(args)
    config = load_config(log)

    report = Locustor()

if __name__ == "__main__":
    main()
