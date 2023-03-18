echo "- No argument"
python whois.py

echo "- One argument: string"
python whois.py "foo"

echo "- One argument: float"
python whois.py 3.14

echo "- One argument: boolean"
python whois.py True

echo "- One argument: even integer"
python whois.py 42

echo "- One argument: odd integer"
python whois.py 43

echo "- One argument: negative integer"
python whois.py -42

echo "- One argument: zero"
python whois.py 0

echo "- Two arguments"
python whois.py "foo" "bar"

echo "- Three arguments"
python whois.py "foo" "bar" "baz"