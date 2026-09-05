module.exports = {
  default: {
    requireModule: ['ts-node/register'],
    require: [
      'src/stepDefinitions/*.ts',
      'src/hooks/*.ts'
    ],
    paths: [
      'src/features/*.feature'
    ],
    format: [
      'progress',
      'json:reports/cucumber-report.json'
    ]
  }
};