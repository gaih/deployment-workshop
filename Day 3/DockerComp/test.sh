sleep 5
if curl -i "http://127.0.0.1:5000/" 2>&1 | grep -w "200\|301"; then
  echo "Tests passed!"
  exit 0
else
  echo "Tests failed!"
  exit 1
fi
