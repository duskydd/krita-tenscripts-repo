## 
## how to use: after making a selection in krita, run the script to make a copy of the selection as 
## a new layer, and then hide the original layer. Afterwards,set the move tool.
## useful helping with automatic isolation of selections
from krita import *
from PyQt5 import QtWidgets, QtCore, uic
def copySelectAndHide():
    app = Krita.instance()
    active = Krita.instance().activeDocument().activeNode()
    doc = app.activeDocument()
    root = doc.rootNode()
    selection = doc.selection()
    if (selection is None):
        QMessageBox.information(QWidget(), i18n("Python Custom Script Error:copymove.py"), i18n("No object selected"))
        return  
    newNode = doc.createNode('selection','paintLayer')
    selection.copy(active)
    selection.paste(newNode,selection.x(),selection.y())
    root.addChildNode(newNode,None)
    active.setVisible(False)
    root.removeChild(active)
    Krita.instance().action('deselect').trigger()
    Krita.instance().action('KritaTransform/KisToolMove').trigger()
    Krita.instance().activeDocument().refreshProjection()

copySelectAndHide()