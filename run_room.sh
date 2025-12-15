#!/bin/bash

set -e

echo "Starting Room System"

ROOT="$(cd "$(dirname "$0")" && pwd)"
ROOM_NODE="$ROOT/src/room_node"
VENV_PATH="$ROOT/venv/bin/activate"

echo "Running Sensor Logger"
/usr/bin/python3 "$ROOM_NODE/sensor_logger.py" & PID_SENSOR_LOGGER=$!

if [ ! -f "$VENV_PATH" ]; then
   python3 -m venv venv
   pip install -r requirements.txt
fi

echo "Running AI Prediction Logger"
source "$ROOT/venv/bin/activate"
"$ROOT/venv/bin/python" "$ROOM_NODE/prediction_logger.py" & PID_AI_PRED_LOGGER=$!

echo "Running Result Display"
/usr/bin/python3 "$ROOM_NODE/display_result.py" & PID_RESULT_DISPLAY=$!

echo "Running Joystick Input"
/usr/bin/python3 "$ROOM_NODE/joystick_input.py" & PID_JOYSTICK_INPUT=$!

trap 'echo "Stopping Room System"; \
kill $PID_SENSOR_LOGGER $PID_RESULT_DISPLAY $PID_AI_PRED_LOGGER $PID_JOYSTICK_INPUT; \
exit' SIGINT SIGTERM

wait