read -n 1 name

case $name in
    [Yy])
    echo "YES"
    ;;
    *)
    echo "NO"
esac
