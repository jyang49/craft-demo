bucket=jason-test-2018-0816-1
files=file_list.txt

ls out > $files

for file in `cat $files`
do
  echo "put $file"
  aws s3api put-object --bucket $bucket --key $file --body out/$file
done
