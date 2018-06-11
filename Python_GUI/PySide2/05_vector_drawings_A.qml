import QtQuick 2.0

Rectangle {
    id: main
    width: 320
    height: 240
    color: "lightgray"

    Image {
        id: left_image
        source: "editors/vim.svg"
        width: 200
        height: 200
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Image {
        id: center_image
        source: "editors/emacs.svg"
        width: 200
        height: 200
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Image {
        id: right_image
        source: "editors/atom.svg"
        width: 200
        height: 200
        anchors.horizontalCenter: parent.horizontalCenter
    }
}
