from os import listdir, remove, getcwd
from platform import system
from shutil import unpack_archive
from wget import download
from requests import get

class InstallChromeDriver():
  def __init__(self):
    self.system = system()
  
  def get_chrome_version_root(self):
    if self.system == 'Darwin':
    #FOR MAC
      infoFileContents = []
      with open('/Applications/Google Chrome.app/Contents/Info.plist', 'r') as xmlInfoFile:
        for line in xmlInfoFile:
          lineWithoutBreaks = line.replace('\n', '').replace('\t', '')
          infoFileContents.append(lineWithoutBreaks)

      keyIndex = infoFileContents.index('<key>KSVersion</key>')
      versionNumberFull = infoFileContents[keyIndex + 1].replace('<string>', '').replace('</string>', '')
      versionNumberRoot = versionNumberFull[:3]
    
    elif self.system == 'Windows':
      #FOR WIN
      versionNumberFull = listdir("C:\\Program Files (x86)\\Google\\Chrome\\Application")[0]
      versionNumberRoot = versionNumberFull[:3]
    
    else:
      print('Error! Unsupported OS to run script')

    return versionNumberRoot

  def install_chromedriver(self):
    currentVersionRoot = self.get_chrome_version_root()
    latestChromeDriverVersion = get(f'https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_{currentVersionRoot}').text
    
    if self.system == 'Darwin':
      localChromeDriverDirectory = getcwd() + '/bin/chrome_driver/'
    
      try:
        remove(localChromeDriverDirectory + 'chrome-mac-arm64/')
      except FileNotFoundError:
        print('Previous ChromeDriver already removed!')

      download(f'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{latestChromeDriverVersion}/mac-arm64/chrome-mac-arm64.zip', localChromeDriverDirectory)
      unpack_archive(filename=localChromeDriverDirectory + '/chrome-mac-arm64.zip', extract_dir=localChromeDriverDirectory, format='zip')
      remove(localChromeDriverDirectory + 'chrome-mac-arm64.zip')
      
      print("Successfully installed latest version of Chrome Driver")

    elif self.system == 'Windows':
      localChromeDriverDirectory = getcwd() + '\\bin\\chrome_driver\\'

      try:
        remove(localChromeDriverDirectory + "chrome-win64\\")
      except FileNotFoundError:
        print('Previous ChromeDriver already removed!')
      
      download(f'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{latestChromeDriverVersion}/win64/chrome-win64.zip', localChromeDriverDirectory)
      unpack_archive(filename=localChromeDriverDirectory + '\\chrome-win64.zip', extract_dir=localChromeDriverDirectory, format='zip')
      remove(localChromeDriverDirectory + 'chrome-win64.zip')
      
      print("Successfully installed latest version of Chrome Driver")

    else:
      print('Error! Unsupported OS to run script')
    
    