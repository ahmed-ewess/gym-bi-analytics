-- Star Schema for Gym BI Analytics

CREATE TABLE DimMember (
  MemberID INT PRIMARY KEY,
  Age INT,
  Gender VARCHAR(1),
  PaymentMethod VARCHAR(20)
);

CREATE TABLE DimMembershipType (
  MembershipType VARCHAR(20) PRIMARY KEY,
  MonthlyFee DECIMAL(10,2)
);

CREATE TABLE FactMembershipActivity (
  MemberID INT,
  MembershipType VARCHAR(20),
  JoinDate DATE,
  LastVisitDate DATE,
  VisitsLast30Days INT,
  PersonalTrainingSessionsLast90Days INT,
  InactivityDays INT,
  Cancelled INT,
  FOREIGN KEY (MemberID) REFERENCES DimMember(MemberID),
  FOREIGN KEY (MembershipType) REFERENCES DimMembershipType(MembershipType)
);