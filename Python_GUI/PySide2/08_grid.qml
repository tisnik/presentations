import QtQuick 2.0


Rectangle {
    id: main
    width: 320
    height: 240
    color: "lightgray"

    Grid {
        columns: 3
        spacing: 2
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter

        Rectangle {
            color: "#ff8080"
            width: 75
            height: 75
        }

        Rectangle {
            color: "yellow"
            width: 32
            height: 75
        }

        Rectangle {
            color: "#8080ff"
            width: 75
            height: 32
        }

        Rectangle {
            color: "#8080ff"
            width: 75
            height: 75
        }

        Rectangle {
            color: "black"
            width: 10
            height: 10
        }

        Image {
            id: left_image
            source: "editors/vim.svg"
            width: 100
            height: 100
        }
    }
}
