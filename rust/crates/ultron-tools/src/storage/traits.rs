//! MemoryBackend trait for all storage backends.

use ultron_core::{UltronError, RetrievalResult};
use serde_json::Value;

pub trait MemoryBackend: Send + Sync {
    fn backend_id(&self) -> &str;
    fn store(
        &self,
        content: &str,
        source: &str,
        metadata: Option<&Value>,
    ) -> Result<String, UltronError>;
    fn retrieve(
        &self,
        query: &str,
        top_k: usize,
    ) -> Result<Vec<RetrievalResult>, UltronError>;
    fn delete(&self, doc_id: &str) -> Result<bool, UltronError>;
    fn clear(&self) -> Result<(), UltronError>;
    fn count(&self) -> Result<usize, UltronError>;
}
