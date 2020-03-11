#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod

class ProjectWork(object):

    def __init__(self, desc = ""):
        self.description = desc

    def setName(self, name):
        self.description += "Project Name: " + name + "\n"

    def setTestDir(self, tst):
        self.description += "Project Test Dir: " + tst + "\n"

    def createDirTree(self, tree):
        self.description += "Project Dir Tree: " + tree + "\n"

    def showState(self):
        return self.description


class Builder(object):
    __metaclass__ = ABCMeta    

    @abstractmethod
    def setProjectName(self, name):
        pass

    @abstractmethod
    def setProjectTestDir(self, pdir):
        pass

    @abstractmethod
    def setProjectDirTree(self, dtree):
        pass

    @abstractmethod
    def getProjectInfo(self):
        pass

class SimpleProjectBuilder(Builder):

    def __init__(self):
        self.project = ProjectWork("Simple Project!")

    def setProjectName(self, name):
        self.project.setName("Simple " + name)

    def setProjectTestDir(self, tdir):
        self.project.setTestDir("no test dir")

    def setProjectDirTree(self, tdir):
        self.project.createDirTree("no dir tree")

    def getProjectInfo(self):
        return self.project


class BigProjectBuilder(Builder):

    def __init__(self):
        self.project = ProjectWork("Big Project!")

    def setProjectName(self, name):
        self.project.setName("Big " + name)

    def setProjectTestDir(self, tdir):
        self.project.setTestDir("Test dir for product " + tdir)
        self.project.setTestDir("Test dir for modules " + tdir)
        self.project.setTestDir("Test dir for GUI " + tdir)

    def setProjectDirTree(self, tdir):
        self.project.createDirTree("Dir tree " + tdir)

    def getProjectInfo(self):
        return self.project


class Client(object):
    
    def __init__(self, name):
        self.name = name
        self.builder = None

    def setBuilder(self, builder):
        self.builder = builder

    def setupProject(self):
        self.builder.setProjectName(self.name)
        self.builder.setProjectTestDir(self.name)
        self.builder.setProjectDirTree(self.name)

    def showProject(self):
        print(self.builder.getProjectInfo().showState())


if __name__ == '__main__':
    c1 = Client("Budujemy Stolyce :-)")
    #c1.setBuilder(BigProjectBuilder())
    c1.setBuilder(SimpleProjectBuilder())
    c1.setupProject()
    c1.showProject()
