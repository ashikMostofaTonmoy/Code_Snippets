for f in *.tif; do
     gdal_translate "$f" "${f%.*}.png"
done