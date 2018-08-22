# must first run following command
# source venv_template/bin/activate

ls ../setup/objects/out/ > list
for f in `cat list`
do
  echo "insert $f"
  python3 put_item.py $f
done
