from PySide6.QtCore import QImage
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Property, QImage, QPixmap, Qt
from PySide6.QtWidgets import QWizard, QGridLayout, QPixmap, QLineEdit, QWizardPage, QLabel, QVBoxLayout, QgsProjectionSelectionTreeWidget

icon_path = '/home/nyall/nr_logo.png'
 
class ProjectWizard(QWizard):
     
    def __init__(self, parent=None):
        super().__init__(parent)
         
        self.addPage(Page1(self))
        self.addPage(Page2(self))
        self.setWindowTitle("New Project")
         
        logo_image=QImage('path_to_logo.png')
        self.setPixmap(QWizard.LogoPixmap, QPixmap.fromImage(logo_image))
         
        self.setOption(QWizard.NoCancelButton, True)
        self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
    def reject(self):
        pass

class Page1(QWizardPage):
     
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle('General Properties')
        self.setSubTitle('Enter general properties for this project.')
 
        # create some widgets
        self.project_number_line_edit = QLineEdit()
        self.project_title_line_edit = QLineEdit()
        self.author_line_edit = QLineEdit()        
         
        # set the page layout
        layout = QGridLayout()
        layout.addWidget(QLabel('Project Number'),0,0)
        layout.addWidget(self.project_number_line_edit,0,1)
        layout.addWidget(QLabel('Title'),1,0)
        layout.addWidget(self.project_title_line_edit,1,1)
        layout.addWidget(QLabel('Author'),2,0)
        layout.addWidget(self.author_line_edit,2,1)
        self.setLayout(layout)
         
        self.registerField('number*',self.project_number_line_edit)
        self.registerField('title*',self.project_title_line_edit)
        self.registerField('author*',self.author_line_edit)
  
  
class Page2(QWizardPage):
     
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle('Project Coordinate System')
        self.setSubTitle('Choosing an appropriate projection is important to ensure accurate distance and area measurements.')
         
        self.proj_selector = QgsProjectionSelectionTreeWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.proj_selector)
        self.setLayout(layout)
         
        self.registerField('crs',self.proj_selector)
        self.proj_selector.crsSelected.connect(self.crs_selected)
         
    def crs_selected(self):
        self.setField('crs',self.proj_selector.crs())
        self.completeChanged.emit()
         
    def isComplete(self):
        return self.proj_selector.crs().isValid()
  
         
def runNewProjectWizard():
    d=ProjectWizard()
    d.exec()
     
    # Set the project crs
    crs=d.field('crs')
    QgsProject.instance().setCrs(crs)
     
    # Set the project title
    title=d.field('title')
    QgsProject.instance().setTitle(d.field('title'))
 
    # Create expression variables for the author and project number
    number=d.field('number')
    QgsExpressionContextUtils.setProjectVariable(QgsProject.instance(),'project_number', number)
    author=d.field('author')
    QgsExpressionContextUtils.setProjectVariable(QgsProject.instance(),'project_author', author)
     
     
iface.newProjectCreated.connect(runNewProjectWizard)