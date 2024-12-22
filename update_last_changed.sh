#!/bin/bash
sed -i 's/LAST_UPDATE_TEXT = .*/LAST_UPDATE_TEXT = "Letzter Update '$(date '+%Y-%m-%d')'"/g' pelicanconf.py
pelican content
