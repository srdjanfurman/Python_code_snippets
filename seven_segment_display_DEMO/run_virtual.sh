#!/bin/bash
retVal=$(virtualserialports -l 2)

echo "${retVal}"
