from pydantic import BaseModel

from onyx.configs.constants import DocumentSource


class ConnectorMapping(BaseModel):
    module_path: str
    class_name: str


# Mapping of DocumentSource to connector details for lazy loading
CONNECTOR_CLASS_MAP = {
    DocumentSource.JIRA_SERVICE_MANAGEMENT: ConnectorMapping(
        module_path="onyx.connectors.jira_service_management.connector",
        class_name="JiraServiceManagementConnector",
    ),
    DocumentSource.WEB: ConnectorMapping(
        module_path="onyx.connectors.web.connector",
        class_name="WebConnector",
    ),
    DocumentSource.SLACK: ConnectorMapping(
        module_path="onyx.connectors.slack.connector",
        class_name="SlackConnector",
    ),
    DocumentSource.GITHUB: ConnectorMapping(
        module_path="onyx.connectors.github.connector",
        class_name="GithubConnector",
    ),
    DocumentSource.GOOGLE_DRIVE: ConnectorMapping(
        module_path="onyx.connectors.google_drive.connector",
        class_name="GoogleDriveConnector",
    ),
    DocumentSource.GMAIL: ConnectorMapping(
        module_path="onyx.connectors.gmail.connector",
        class_name="GmailConnector",
    ),
    DocumentSource.BOOKSTACK: ConnectorMapping(
        module_path="onyx.connectors.bookstack.connector",
        class_name="BookstackConnector",
    ),
    DocumentSource.OUTLINE: ConnectorMapping(
        module_path="onyx.connectors.outline.connector",
        class_name="OutlineConnector",
    ),
    DocumentSource.CONFLUENCE: ConnectorMapping(
        module_path="onyx.connectors.confluence.connector",
        class_name="ConfluenceConnector",
    ),
    DocumentSource.JIRA: ConnectorMapping(
        module_path="onyx.connectors.jira.connector",
        class_name="JiraConnector",
    ),
    DocumentSource.PRODUCTBOARD: ConnectorMapping(
        module_path="onyx.connectors.productboard.connector",
        class_name="ProductboardConnector",
    ),
    DocumentSource.SLAB: ConnectorMapping(
        module_path="onyx.connectors.slab.connector",
        class_name="SlabConnector",
    ),
    DocumentSource.CODA: ConnectorMapping(
        module_path="onyx.connectors.coda.connector",
        class_name="CodaConnector",
    ),
    DocumentSource.GITLAB: ConnectorMapping(
        module_path="onyx.connectors.gitlab.connector",
        class_name="GitlabConnector",
    ),
    DocumentSource.CANVAS: ConnectorMapping(
        module_path="onyx.connectors.canvas.connector",
        class_name="CanvasConnector",
    ),
    DocumentSource.GITBOOK: ConnectorMapping(
        module_path="onyx.connectors.gitbook.connector",
        class_name="GitbookConnector",
    ),
    DocumentSource.ZULIP: ConnectorMapping(
        module_path="onyx.connectors.zulip.connector",
        class_name="ZulipConnector",
    ),
    DocumentSource.GURU: ConnectorMapping(
        module_path="onyx.connectors.guru.connector",
        class_name="GuruConnector",
    ),
    DocumentSource.LINEAR: ConnectorMapping(
        module_path="onyx.connectors.linear.connector",
        class_name="LinearConnector",
    ),
    DocumentSource.NOTION: ConnectorMapping(
        module_path="onyx.connectors.notion.connector",
        class_name="NotionConnector",
    ),
    DocumentSource.HUBSPOT: ConnectorMapping(
        module_path="onyx.connectors.hubspot.connector",
        class_name="HubSpotConnector",
    ),
    DocumentSource.DOCUMENT360: ConnectorMapping(
        module_path="onyx.connectors.document360.connector",
        class_name="Document360Connector",
    ),
    DocumentSource.GONG: ConnectorMapping(
        module_path="onyx.connectors.gong.connector",
        class_name="GongConnector",
    ),
    DocumentSource.GOOGLE_SITES: ConnectorMapping(
        module_path="onyx.connectors.google_site.connector",
        class_name="GoogleSitesConnector",
    ),
    DocumentSource.ZENDESK: ConnectorMapping(
        module_path="onyx.connectors.zendesk.connector",
        class_name="ZendeskConnector",
    ),
    DocumentSource.LOOPIO: ConnectorMapping(
        module_path="onyx.connectors.loopio.connector",
        class_name="LoopioConnector",
    ),
    DocumentSource.BOX: ConnectorMapping(
        module_path="onyx.connectors.box.connector",
        class_name="BoxConnector",
    ),
    DocumentSource.DROPBOX: ConnectorMapping(
        module_path="onyx.connectors.dropbox.connector",
        class_name="DropboxConnector",
    ),
    DocumentSource.SHAREPOINT: ConnectorMapping(
        module_path="onyx.connectors.sharepoint.connector",
        class_name="Sharepoint
