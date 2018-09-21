import FWCore.ParameterSet.Config as cms

process = cms.Process("TriggerInfo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
  
# 'root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S13_START53_LV6-v1/00000/0019AB30-B9B7-E311-9E28-003048FF86CA.root'
 # 'file:recosimu1.root'
  
  #'root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/ZZJetsTo4L_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S13_START53_LV6-v1/00000/4033B198-8BB8-E311-9F9F-0025905A605E.root'
  #'root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/VBFToHToZZTo2L2Nu_M-450_7TeV-powheg15-pythia6/AODSIM/PU_S13_START53_LV6-v1/00000/0AE64C55-1FC8-E311-9E77-002481E15008.root'
 #'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/AOD/12Oct2013-v1/10000/000D143E-9535-E311-B88B-002618943934.root',
 #'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/AOD/12Oct2013-v1/10001/CC4E8182-6A37-E311-BB75-0025905964CC.root',
 #'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/AOD/12Oct2013-v1/20000/C820A0DE-053F-E311-844A-002590596484.root'

  #'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/Photon/AOD/12Oct2013-v1/10000/B4770060-823E-E311-BA5E-02163E007964.root',  # electron
#  'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/Photon/AOD/12Oct2013-v1/20001/5E8CD7A6-223A-E311-8CDC-0025904B26A8.root',
 # 'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/Photon/AOD/12Oct2013-v1/20002/FC01A687-723B-E311-8CD6-003048CF9E96.root'
 #'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/AOD/12Oct2013-v1/10000/0020AF81-A835-E311-97DC-00261894398C.root' # muon
 #'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/AOD/12Oct2013-v1/10000/F677BF37-9435-E311-8CF1-003048678B0E.root'
 
 #'file:simu.root'
 
 ##'root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/ZZJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S13_START53_LV6-v1/020000/C4173C05-BFB6-E311-9F30-002618943913.root'
 
 #'root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/WZJetsTo3LNu_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S13_START53_LV6-v1/00000/0013A453-7ABD-E311-AAC9-0025905A60F8.root'
 
 
 
 
  #  'root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/ZZTo2e2mu_7TeV_mll8_mZZ95-160-powheg15-pythia6/AODSIM/PU_S13_START53_LV6-v1/020000/30FDADFE-4C9D-E411-977F-00266CFFBF30.root'

#'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/Photon/AOD/12Oct2013-v1/20000/009BB2E2-F738-E311-A58F-002481E0E184.root'

'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/Photon/AOD/12Oct2013-v1/10000/AC980FCC-943D-E311-A1D6-003048F11824.root'
#' root://eospublic.cern.ch//eos/opendata/cms/Run2011A/ElectronHad/AOD/12Oct2013-v1/20001/001F9231-F141-E311-8F76-003048F00942.root' 
#    'file:00082EAF-C03D-E311-8E53-003048F00B1C.root' 
    )
)

#needed to get the actual prescale values used from the global tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA.db')
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/START53_LV6A1.db')
#process.GlobalTag.globaltag = 'FT_53_LV5_AN1::All'
process.GlobalTag.globaltag = 'START53_LV6A1::All'

#configure the analyzer
process.gettriggerinfo = cms.EDAnalyzer('TriggerInfoAnalyzer',
                              processName = cms.string("HLT"),
                              triggerName = cms.string("@"),         
                              datasetName = cms.string("SingleMu"),           
                              triggerResults = cms.InputTag("TriggerResults","","HLT"),
                              triggerEvent   = cms.InputTag("hltTriggerSummaryAOD","","HLT")                             
                              )


process.triggerinfo = cms.Path(process.gettriggerinfo)
process.schedule = cms.Schedule(process.triggerinfo)
