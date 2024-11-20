pants --tag='final' package ::

BLUE='\e[34m'
RED='\e[31m'
RESET='\e[0m'

FINAL_IMAGES=(
    "myapp-362-image"
    "myapp-384-image"
)

ERROR_FLAG=0
for image in "${FINAL_IMAGES[@]}"; do
    echo -e "${BLUE}INFO: Running Docker image: ${image}${RESET}"
    docker run --rm "$image" 

    exit_code=$?
    if [ $exit_code -ne 0 ]; then
        echo -e "${RED}ERROR: Container for $image exited with code: ${exit_code}.${RESET}"
        ERROR_FLAG=1
    fi
done

if [ $ERROR_FLAG -ne 0 ]; then
    exit 1
fi
