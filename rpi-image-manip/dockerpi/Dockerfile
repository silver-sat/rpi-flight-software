FROM lukechilds/dockerpi:vm

ADD https://raw.githubusercontent.com/dhruvvyas90/qemu-rpi-kernel/9fb4fcf463df4341dbb7396df127374214b90841/kernel-qemu-5.10.63-bullseye /root/qemu-rpi-kernel/
ADD https://raw.githubusercontent.com/dhruvvyas90/qemu-rpi-kernel/9fb4fcf463df4341dbb7396df127374214b90841/versatile-pb-bullseye-5.10.63.dtb /root/qemu-rpi-kernel/

ADD ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
